import speech_recognition as sr
import pyautogui

KEYWORD_MAP = {
    'up': 'w',
    'down': 's',
    'right': 'd',
    'left': 'a',
    'space': 'space',
    'lump': ('space', 'a'),
    'rump': ('space', 'd'),
}

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=2)
            text = recognizer.recognize_google(audio)
            return text.strip()
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            return None

def press_key(key):
    pyautogui.press(key)

def press_hotkeys(keys):
    pyautogui.hotkey(*keys)

def process_sentence(sentence):
    for keyword, action in KEYWORD_MAP.items():
        if keyword in sentence.lower():
            if isinstance(action, tuple):
                press_hotkeys(action)
            elif action == 'space':
                press_key(action)
            else:
                pyautogui.write(action)
            return