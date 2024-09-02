import sys
from VoiceControls import recognize_speech, process_sentence
from MouseControls import move_mouse, left_click, right_click, middle_click

def handle_voice_commands(sentence):
    if 'look' in sentence.lower():
        for direction, (dx, dy) in DIRECTION_MAP.items():
            if direction in sentence.lower():
                try:
                    parts = sentence.lower().split()
                    if len(parts) > 2 and parts[2].isdigit():
                        duration = float(parts[2])
                    else:
                        duration = 1
                    move_mouse(dx, dy, duration)
                except ValueError:
                    pass
                return
    
    if 'right click' in sentence.lower():
        right_click()
    elif 'left click' in sentence.lower():
        left_click()
    elif 'middle click' in sentence.lower():
        middle_click()
    else:
        process_sentence(sentence)

if __name__ == "__main__":
    DIRECTION_MAP = {
        'right': (10, 0),
        'left': (-10, 0),
        'up': (0, -10),
        'down': (0, 10),
    }

    while True:
        sentence = recognize_speech()
        if sentence:
            if sentence.lower() == "stop program":
                print("Stopping the program...")
                sys.exit()
            handle_voice_commands(sentence)