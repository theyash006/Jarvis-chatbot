GEMINI_API_KEY = "your_gemini_api_key_here"

# ── ElevenLabs (OPTIONAL — premium voice quality) ───────────
# Leave as "" to use the free built-in pyttsx3 voice
# Keys → https://elevenlabs.io → Profile → API Keys
ELEVENLABS_API_KEY  = ""
ELEVENLABS_VOICE_ID = ""

# ── Picovoice (OPTIONAL — always-on hardware wake word) ─────
# Leave as "" to use the built-in software wake word (works fine)
# Free key → https://console.picovoice.ai
PICOVOICE_KEY = ""

# ════════════════════════════════════════════════════════════
#  Everything below is managed automatically — do not edit
# ════════════════════════════════════════════════════════════
ASSISTANT_NAME = "Jarvis"
USER_NAME      = "Sir"        # overwritten from user_profile.json at startup
USER_GENDER    = "male"
USER_AGE       = ""
USER_CITY      = ""
WAKE_WORD      = "jarvis"

GEMINI_MODEL       = "gemini-2.5-flash-preview-05-20"
GEMINI_MAX_TOKENS  = 1024
GEMINI_TEMPERATURE = 0.7

STT_ENGINE           = "google"
WHISPER_MODEL        = "base"
MIC_ENERGY_THRESHOLD = 300
MIC_PAUSE_THRESHOLD  = 1.0
LISTEN_TIMEOUT       = 8

TTS_ENGINE          = "pyttsx3"
PYTTSX3_RATE        = 175
PYTTSX3_VOLUME      = 1.0
PYTTSX3_VOICE_INDEX = 0

WINDOW_WIDTH      = 1120
WINDOW_HEIGHT     = 740
WINDOW_TITLE      = "J.A.R.V.I.S — AI Assistant"
MAX_CHAT_HISTORY  = 100
MAX_CONTEXT_TURNS = 20

APP_PATHS = {
    "chrome": "chrome", "google chrome": "chrome",
    "firefox": "firefox", "edge": "msedge",
    "notepad": "notepad", "calculator": "calc",
    "vs code": "code", "vscode": "code",
    "visual studio code": "code",
    "file explorer": "explorer", "explorer": "explorer",
    "word": "winword", "excel": "excel",
    "powerpoint": "powerpnt", "spotify": "spotify",
    "discord": "discord", "telegram": "telegram",
    "whatsapp": "whatsapp", "cmd": "cmd",
    "terminal": "cmd", "paint": "mspaint",
    "task manager": "taskmgr", "settings": "ms-settings:",
}

LOG_DIR   = "logs"
LOG_LEVEL = "INFO"
