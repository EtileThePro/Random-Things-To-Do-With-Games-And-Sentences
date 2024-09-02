import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = recognizer.listen(source)
    print("You said: " + recognizer.recognize_google(audio))