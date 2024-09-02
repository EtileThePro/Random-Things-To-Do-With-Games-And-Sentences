import os
import sys
import speech_recognition as sr
from gtts import gTTS
import subprocess

tts_dir = "TTS"
if not os.path.exists(tts_dir):
    os.makedirs(tts_dir)

log_file_path = "sentences.txt"
recognizer = sr.Recognizer()
volume_change_dB = 100
use_adjusted_audio = False

def log_sentence(sentence):
    with open(log_file_path, "a") as file:
        file.write(sentence + "\n")

def check_repeated(sentence):
    if not os.path.exists(log_file_path):
        return False

    with open(log_file_path, "r") as file:
        logged_sentences = file.readlines()

    return sentence.strip() in (line.strip() for line in logged_sentences)

def generate_tts(sentence, tts_dir):
    tts = gTTS(f"YOU REPEATED A SENTENCE YOU SAID {sentence} TWICE BECAUSE OF THAT I'M SHUTTING DOWN YOU'VE KILLED ME. YOU DAMN NIGGER ASS NIGGA AHHH")
    tts_file_path = os.path.join(tts_dir, "repeated_sentence.mp3")
    tts.save(tts_file_path)
    if use_adjusted_audio:
        adjusted_file_path = tts_file_path.replace(".mp3", "_adjusted.mp3")
        command = [
            'ffmpeg',
            '-i', tts_file_path,
            '-filter:a', f'volume={volume_change_dB}dB',
            adjusted_file_path
        ]
        subprocess.run(command, check=True)
        os.remove(tts_file_path)
        return adjusted_file_path
    return tts_file_path

def play_audio(tts_file_path):
    if use_adjusted_audio:
        command = ['mpg123', tts_file_path]
    else:
        command = ['mpg123', tts_file_path]
    subprocess.run(command, check=True)

def clear_log_file():
    with open(log_file_path, "w") as file:
        pass

def listen_and_process():
    tts_file_path = None
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        while True:
            try:
                audio = recognizer.listen(source)
                sentence = recognizer.recognize_google(audio)
                
                print(f"Recognized: {sentence}")
                
                if check_repeated(sentence):
                    tts_file_path = generate_tts(sentence, tts_dir)
                    play_audio(tts_file_path)
                    os.remove(tts_file_path)
                    break

                log_sentence(sentence)
                print("Listening...")
                
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                break
    
    clear_log_file()
    print("Cleared the log file.")

if __name__ == '__main__':
    listen_and_process()




#BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOLLLLLLLLLLLLLLLLLLLLLLLLLLEEEEEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANNNNNNNNNNNNNNN