#!/usr/bin/env python3
# ============================================================
#  setup.py — JARVIS One-Click Setup Script
# ============================================================
#  Run this ONCE before first launch:
#      python setup.py
# ============================================================

import os
import sys
import subprocess
import platform
import shutil

OS = platform.system()

BANNER = """
╔══════════════════════════════════════════════════════════╗
║           J A R V I S   S E T U P   W I Z A R D         ║
╚══════════════════════════════════════════════════════════╝
"""

def run(cmd, check=True):
    print(f"\n  → {' '.join(cmd)}")
    result = subprocess.run(cmd, check=check, capture_output=False)
    return result.returncode == 0

def check_python():
    print("\n[1/5] Checking Python version…")
    v = sys.version_info
    if v.major < 3 or (v.major == 3 and v.minor < 10):
        print(f"  ❌ Python 3.10+ required. You have {v.major}.{v.minor}")
        print("     Download from: https://python.org/downloads")
        sys.exit(1)
    print(f"  ✅ Python {v.major}.{v.minor}.{v.micro}")

def install_portaudio():
    """Pre-install portaudio (required by pyaudio) on Mac/Linux."""
    print("\n[2/5] Installing system audio dependencies…")
    if OS == "Darwin":
        if shutil.which("brew"):
            run(["brew", "install", "portaudio"], check=False)
            print("  ✅ portaudio installed via Homebrew")
        else:
            print("  ⚠️  Homebrew not found. Install it from https://brew.sh then run:")
            print("       brew install portaudio")
    elif OS == "Linux":
        run(["sudo", "apt-get", "install", "-y", "portaudio19-dev", "python3-pyaudio"], check=False)
        print("  ✅ portaudio19-dev installed")
    else:
        print("  ℹ️  Windows — PyAudio will install via pip")

def install_requirements():
    print("\n[3/5] Installing Python packages…")
    print("  This may take 2–5 minutes depending on your internet speed.\n")

    pip = [sys.executable, "-m", "pip", "install", "--upgrade"]

    # Install in order (some have build dependencies)
    packages = [
        ["pip", "setuptools", "wheel"],
        ["pyaudio"],
        ["google-generativeai"],
        ["SpeechRecognition"],
        ["pyttsx3"],
        ["PyQt6"],
        ["pyautogui"],
        ["psutil"],
        ["pywhatkit"],

        ["requests", "Pillow", "numpy"],
    ]

    # Windows-specific
    if OS == "Windows":
        packages.append(["pycaw", "comtypes"])

    failed = []
    for pkg_list in packages:
        success = run(pip + pkg_list, check=False)
        if not success:
            failed.append(pkg_list)

    if failed:
        print(f"\n  ⚠️  Some packages failed: {failed}")
        print("      You can install them manually later.")
    else:
        print("\n  ✅ All packages installed successfully")

def create_env_file():
    print("\n[4/5] Creating .env configuration file…")
    if os.path.exists(".env"):
        print("  ℹ️  .env already exists — skipping")
        return

    shutil.copy(".env.example", ".env")
    print("  ✅ Created .env from template")

    # Prompt for API key
    print("\n  ─────────────────────────────────────────────────────")
    print("  To use JARVIS you need a free Google Gemini API key.")
    print("  Get one at: https://aistudio.google.com/app/apikey")
    print("  ─────────────────────────────────────────────────────")
    key = input("\n  Paste your Gemini API key (or press Enter to skip): ").strip()

    if key:
        with open(".env", "r") as f:
            content = f.read()
        content = content.replace("your_gemini_api_key_here", key)
        with open(".env", "w") as f:
            f.write(content)
        print("  ✅ API key saved to .env")
    else:
        print("  ⚠️  Skipped — edit .env manually before running JARVIS")

def create_logs_dir():
    print("\n[5/5] Creating directories…")
    os.makedirs("logs", exist_ok=True)
    os.makedirs("assets", exist_ok=True)
    print("  ✅ Directories ready")

def print_next_steps():
    print("""
╔══════════════════════════════════════════════════════════╗
║                   S E T U P   D O N E !                  ║
╚══════════════════════════════════════════════════════════╝

  Next steps:

  1. Make sure your .env file has a valid GEMINI_API_KEY
     → Edit .env with any text editor

  2. Launch JARVIS:
     → python main.py

  3. Say the wake word to activate:
     → "Jarvis, open Chrome"
     → "Jarvis, what's the weather in Delhi?"
     → "Jarvis, play lofi music on YouTube"
     → "Jarvis, search Python tutorials"

  Tips:
  • Click the 🎤 button for push-to-talk
  • Type commands in the text box too
  • Say "Jarvis, help" for a list of commands

  Docs:  See README.md for full command reference
""")

if __name__ == "__main__":
    print(BANNER)
    check_python()
    install_portaudio()
    install_requirements()
    create_env_file()
    create_logs_dir()
    print_next_steps()
