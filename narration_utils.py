import pyttsx3

def narrate_location(text, language="English"):
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
    
    # Select voice based on language
    if language == "Hindi":
        for voice in voices:
            if "hindi" in voice.name.lower() or "hi" in voice.languages:
                engine.setProperty('voice', voice.id)
                break
    elif language == "Marathi":
        for voice in voices:
            if "marathi" in voice.name.lower() or "mr" in voice.languages:
                engine.setProperty('voice', voice.id)
                break
    else:
        # Default to English
        for voice in voices:
            if "english" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

    engine.setProperty('rate', 160)  # Set speech rate
    engine.say(text)
    engine.runAndWait()
