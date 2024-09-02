import speech_recognition as sr
import pyautogui
from gtts import gTTS
import os
import sys

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say a sentence...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            return text.strip()
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def text_to_speech(text, filename):
    if not os.path.exists("TTS"):
        os.makedirs("TTS")
    tts_path = os.path.join("TTS", filename)
    tts = gTTS(text=text, lang='en')
    tts.save(tts_path)
    os.system(f"mpg123 {tts_path}")
    os.remove(tts_path)

def type_sentence(sentence):
    pyautogui.write(sentence)

if __name__ == "__main__":
    while True:
        sentence = recognize_speech()
        if sentence:
            print(f"Recognized sentence: {sentence}")
            if sentence.lower() == "stop program":
                text_to_speech("Stopping the program", "stopping_program.mp3")
                print("Exiting program...")
                sys.exit()
            type_sentence(sentence)