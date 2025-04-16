import pyttsx3
from gtts import gTTS
import os
import tempfile

def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        pass

def speak_text_multilingual(text, lang):
    lang_codes = {"Hindi": "hi", "Marathi": "mr"}
    if lang in lang_codes:
        tts = gTTS(text=text, lang=lang_codes[lang])
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            os.system(f"start {fp.name}")

