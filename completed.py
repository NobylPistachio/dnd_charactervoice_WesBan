import logging

from SpeechToTextToSpeech import SpeechToText,TextToSpeech_aeiou
from soundOutput import playAudio_Pyaudio, main

def speech_to_text_to_speech():
    text = SpeechToText()
    TextToSpeech_aeiou(text)
    playAudio_Pyaudio("output.wav")

def tts_aeiou(text):
    TextToSpeech_aeiou(text)
    print("done")
    playAudio_Pyaudio("output.wav")

def main_speechToTextToSpeech():
    print("Speech to Text to Speech script has been started.")
    while True:
        text = SpeechToText()
        TextToSpeech_aeiou(text)
        playAudio_Pyaudio("output.wav")
        input()

def main_textOnly():
    while True:
        text = input("Wes Ban:\t")
        TextToSpeech_aeiou(text)
        print("Playing")
        playAudio_Pyaudio("output.wav")
        print("Done")

def play_song():
    playAudio_Pyaudio("Main.wav")

def self_song():
    pass

if __name__ == "__main__":
    #main_textOnly()
    play_song()