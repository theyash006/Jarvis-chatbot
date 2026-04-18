import os, sys, logging, threading
from datetime import datetime
from pathlib import Path

Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(f"logs/jarvis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
        logging.StreamHandler(sys.stdout),
    ]
)
logger = logging.getLogger("JARVIS")

print("""
╔══════════════════════════════════════════════════════════╗
║       J . A . R . V . I . S   A I   A S S I S T A N T   ║
║              Powered by Google Gemini 2.5                ║
╚══════════════════════════════════════════════════════════╝
""")

try:
    import config
    from core.voice      import VoiceEngine
    from core.ai_brain   import AIBrain
    from core.automation import Automation
    from core.ui         import AppShell
    from core.user_profile import load as load_profile
except ImportError as e:
    print(f"❌ Import error: {e}\n   Run: pip install -r requirements.txt")
    sys.exit(1)

try:
    from PyQt6.QtWidgets import QApplication
    from PyQt6.QtCore    import QTimer
except ImportError:
    print("❌ PyQt6 not installed.  Run: pip install PyQt6")
    sys.exit(1)


class JarvisCore:
    def __init__(self, shell: AppShell):
        self.shell  = shell
        self.ai     = None
        self.voice  = None
        self.auto   = Automation()
        self._busy  = False

    def initialize(self):
        # AI Brain
        try:
            self.ai = AIBrain()
            profile = load_profile()
            from core.user_profile import get_salutation
            salut   = get_salutation(profile)
            self.shell.add_message(
                "assistant",
                f"All systems online. Good to see you, {salut}. "
                f"Say '{config.WAKE_WORD}' or type below to begin."
            )
        except ValueError as e:
            self.shell.add_message("assistant", str(e))
            self.shell.set_status("error")
            return False

        # Voice engine
        self.voice = VoiceEngine(
            on_command_callback=self.on_command,
            on_status_callback=self.shell.set_status,
        )
        self.shell.set_mic_callback(self._on_ptt)
        self.shell.on_mute_change = self._on_mute_change
        self.voice.start_listening()
        logger.info("✅ JARVIS ready")
        return True

    def on_command(self, text: str):
        if not text or not text.strip() or self._busy:
            return
        self._busy = True
        try:
            self.shell.add_message("user", text)
            self.shell.set_status("processing")
            result = self.ai.process(text)
            spoken = result.get("spoken", "I'm not sure how to help with that.")
            action = result.get("action")

            if action:
                ar = self.auto.execute(action)
                if not ar.get("success"):
                    spoken = f"I tried, but ran into an issue: {ar.get('message','unknown error')}"

            self.shell.add_message("assistant", spoken)
            if self.voice and not getattr(self.voice, '_muted', False):
                self.voice.speak(spoken)
        except Exception as e:
            logger.error(f"Command error: {e}", exc_info=True)
            self.shell.add_message("assistant", "I encountered an unexpected error.")
            self.shell.set_status("error")
        finally:
            self._busy = False
            self.shell.set_status("idle")

    def on_text_command(self, text: str):
        self.on_command(text)

    def _on_ptt(self):
        if self._busy:
            return
        def _listen():
            self.shell.set_status("listening")
            text = self.voice.listen_once() if self.voice else None
            if text:
                self.on_command(text)
            else:
                self.shell.set_status("idle")
                self.shell.add_message("assistant", "I didn't catch that — please try again.")
        threading.Thread(target=_listen, daemon=True).start()

    def _on_mute_change(self, muted: bool):
        if self.voice:
            if muted:
                self.voice.stop_listening()
                self.voice._muted = True
                logger.info("Microphone muted")
            else:
                self.voice._muted = False
                self.voice.start_listening()
                logger.info("Microphone unmuted")

    def shutdown(self):
        if self.voice:
            self.voice.stop_listening()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("JARVIS AI Assistant")

    core_ref = [None]

    def on_text_command(text):
        if core_ref[0]:
            core_ref[0].on_text_command(text)

    shell = AppShell(on_text_command=on_text_command)
    shell.show()

    def deferred_init():
        core = JarvisCore(shell)
        core_ref[0] = core
        core.initialize()

    QTimer.singleShot(600, deferred_init)
    app.aboutToQuit.connect(lambda: core_ref[0].shutdown() if core_ref[0] else None)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
