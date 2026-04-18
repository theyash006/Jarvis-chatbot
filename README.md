# ⚡ JARVIS AI Assistant

> A real JARVIS-style desktop AI assistant — voice-controlled, PC-aware, powered by Google Gemini 2.5

---

## 🗂 Project Structure

```
jarvis/
├── main.py              ← Entry point (run this)
├── config.py            ← All settings (edit here)
├── setup.py             ← One-click installer
├── requirements.txt     ← Python dependencies
├── .env.example         ← API key template
├── .env                 ← Your actual keys (create from .env.example)
│
├── core/
│   ├── voice.py         ← Speech recognition + TTS
│   ├── ai_brain.py      ← Gemini 2.5 AI + conversation memory
│   ├── automation.py    ← System/internet actions
│   └── ui.py            ← PyQt6 JARVIS-style interface
│
├── logs/                ← Auto-generated log files
└── assets/              ← Icons, sounds (optional)
```

---

## 🚀 Quick Start

### Step 1 — Get a Gemini API Key (free)
1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with Google
3. Click **Create API Key** → copy it

### Step 2 — Install & Configure
```bash
# Clone / download this project, then:
cd jarvis

# Run the setup wizard (installs everything automatically)
python setup.py
```
The wizard will ask for your API key and save it to `.env`.

### Step 3 — Launch
```bash
python main.py
```

---

## 🎙 How to Use

### Voice Commands
Say the wake word **"Jarvis"** followed by your command:

| What you say | What happens |
|---|---|
| *"Jarvis, open Chrome"* | Opens Google Chrome |
| *"Jarvis, close Spotify"* | Closes Spotify |
| *"Jarvis, volume up"* | Increases volume by 10% |
| *"Jarvis, set volume to 50"* | Sets volume to 50% |
| *"Jarvis, mute"* | Mutes the system |
| *"Jarvis, play lofi music on YouTube"* | Plays on YouTube |
| *"Jarvis, search Python tutorials"* | Opens Google Search |
| *"Jarvis, open github.com"* | Opens the website |
| *"Jarvis, take a screenshot"* | Saves screenshot to Desktop |
| *"Jarvis, shutdown the computer"* | Schedules shutdown in 5s |
| *"Jarvis, lock the screen"* | Locks Windows/Mac/Linux |
| *"Jarvis, what is quantum computing?"* | Answers with Gemini AI |
| *"Jarvis, tell me a joke"* | Responds conversationally |
| *"Jarvis, write an email for me"* | Types text at cursor |

### Text Commands
Type any command directly into the input box and press **Enter** or click **SEND**.

### Push-to-Talk
Click the **🎤** button to trigger a one-shot listen without using the wake word.

---

## ⚙️ Configuration

Edit `config.py` or `.env` to customise:

| Setting | Default | Description |
|---|---|---|
| `ASSISTANT_NAME` | `Jarvis` | Name the AI uses |
| `USER_NAME` | `Boss` | How AI addresses you |
| `WAKE_WORD` | `jarvis` | Word that activates voice |
| `STT_ENGINE` | `google` | `google` (online) or `whisper` (offline) |
| `TTS_ENGINE` | `pyttsx3` | `pyttsx3` (offline) or `elevenlabs` (premium) |
| `GEMINI_MODEL` | `gemini-2.5-flash-preview-05-20` | Which Gemini model |
| `MIC_ENERGY_THRESHOLD` | `300` | Mic sensitivity (lower = more sensitive) |

### Adding Custom Apps
In `config.py`, add entries to `APP_PATHS`:
```python
APP_PATHS = {
    ...
    "my app": "C:\\Program Files\\MyApp\\myapp.exe",
}
```

---

## 🔧 Troubleshooting

### "PyAudio install failed"
```bash
# Windows:
pip install pipwin
pipwin install pyaudio

# macOS:
brew install portaudio
pip install pyaudio

# Linux:
sudo apt-get install portaudio19-dev
pip install pyaudio
```

### "GEMINI_API_KEY not set"
1. Open `.env` in any text editor
2. Replace `your_gemini_api_key_here` with your actual key
3. Save and restart JARVIS

### Voice recognition not working
- Check microphone permissions in system settings
- Adjust `MIC_ENERGY_THRESHOLD` in `config.py` (lower for quiet mics)
- Try `STT_ENGINE = "whisper"` for offline recognition (more accurate, slower)

### AI not understanding commands
- Be specific: *"open VS Code"* not *"open the code editor"*
- The AI remembers context — you can say *"now close it"* after opening something

### pycaw (Windows volume) errors on non-Windows
- `pycaw` is Windows-only; volume control is automatically skipped on Mac/Linux

---

## 🔊 Upgrading TTS Voice Quality

### Option A: ElevenLabs (best quality, freemium)
1. Sign up at [elevenlabs.io](https://elevenlabs.io)
2. Get API key + Voice ID
3. Add to `.env`:
   ```
   ELEVENLABS_API_KEY=your_key
   ELEVENLABS_VOICE_ID=your_voice_id
   ```
4. In `config.py`: `TTS_ENGINE = "elevenlabs"`

### Option B: Better pyttsx3 Voice (free)
On Windows, install extra voices via **Settings → Time & Language → Speech → Add voices**. Then set `PYTTSX3_VOICE_INDEX = 1` (or 2, 3…) in `config.py`.

---

## 🔌 Offline Mode (Whisper STT)
For fully offline speech recognition (no internet needed for STT):
```python
# In config.py:
STT_ENGINE = "whisper"
WHISPER_MODEL = "base"   # tiny/base/small/medium/large (larger = more accurate, slower)
```
First run will download the model (~145MB for "base").

---

## 📦 Tech Stack

| Component | Library | Why |
|---|---|---|
| AI Brain | Google Gemini 2.5 | Best instruction-following, free tier |
| Speech-to-Text | SpeechRecognition + Whisper | Google online or local offline |
| Text-to-Speech | pyttsx3 / ElevenLabs | Offline default, premium optional |
| UI | PyQt6 | Native, fast, beautiful dark UI |
| Automation | pyautogui + psutil | Cross-platform app/input control |
| Volume | pycaw | Windows audio API |
| Internet | pywhatkit + webbrowser | YouTube, Google, WhatsApp |

---

## 🛣 Upgrade Ideas

- [ ] Whisper streaming (real-time transcription)
- [ ] Picovoice Porcupine wake word (always-on, low CPU)
- [ ] Home automation (Philips Hue, smart plugs)
- [ ] Calendar / email integration (Google APIs)
- [ ] Screen reader / OCR for "what's on my screen?"
- [ ] Custom hotkey (e.g. `Ctrl+Space`) to activate
- [ ] Multi-monitor screenshot with annotation

---

*Built for Yash — aspiring JPL Research Scientist 🚀*
