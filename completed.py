import logging

from SpeechToTextToSpeech import SpeechToText,TextToSpeech_aeiou
from soundOutput import play_audio_to_them, main

def speech_to_text_to_speech():
    text = SpeechToText()
    TextToSpeech_aeiou(text)
    play_audio_to_them("output.wav")

def tts_aeiou(text):
    TextToSpeech_aeiou(text)
    print("done")
    play_audio_to_them("output.wav")

def main_speechToTextToSpeech():
    print("Speech to Text to Speech script has been started.")
    while True:
        text = SpeechToText()
        TextToSpeech_aeiou(text)
        play_audio_to_them("output.wav")
        input()

def main_textOnly():
    while True:
        text = input("Wes Ban:\t")
        TextToSpeech_aeiou(text)
        print("Playing")
        play_audio_to_them("output.wav")
        print("Done")

def play_song():
    play_audio_to_them("Main.wav")

def self_song():
    pass

if __name__ == "__main__":
    #main_textOnly()
    play_song()