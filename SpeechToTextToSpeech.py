import pyaudio
import speech_recognition as sr
from gtts import gTTS
import pygame
import requests
from playsound import playsound

#Thanks to ChatGPT I was able to do this in LITERALLY 1 NIGHT, well almost
#though this does bring up some concerns about the modules, I dont know what they do.


    #Record Audio
def AudioSetup():

    #I dont know what this does, Investigate further

    # Set parameters for audio recording
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    # Create an instance of PyAudio
    p = pyaudio.PyAudio()

    # Open the microphone and start recording
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)



    #Convert Speech to Text
def SpeechToText():
    # Create an instance of the recognizer
    r = sr.Recognizer()

    # Listen to the audio from the microphone
    with sr.Microphone() as source:
        print("Say something...")
        #maybe I can make a button for this so it doesn't auto cut off
        audio = r.listen(source)

    # Convert the audio to text
    text = r.recognize_google(audio)

    return text



    #Convert Text to Speech
def TextToSpeech_Google(text,file_name = 'output.wav'):
    # Create a text-to-speech object
    tts = gTTS(text=text, lang='en')

    # Save the speech as an mp3 file
    tts.save(file_name)

def save_aeiou(input_string):
    import re

    # Define the regular expression pattern
    pattern = r"&"

    # Define the replacement string
    replacement = " and "

    # Use the sub() method of the re module to replace all instances of the pattern with the replacement string
    output_string = re.sub(pattern, replacement, input_string)

    return output_string

def TextToSpeech_aeiou(text,file_name = 'output.wav'):
    
    #NO SYMBOLS

    text = save_aeiou(text)

    url = f'https://tts.cyzon.us/tts?text={text}'
    test = requests.get(url)
    response = test.content

    with open(file_name, mode='bw') as f:
        f.write(response)


    #Play Audio (still looking for something to auto play the sound file)
def PlayAudio_Pygame(file_name = 'output.wav'):
    'This takes a bit long but it works'
    # Initialize Pygame
    pygame.init()

    # Load the mp3 file
    pygame.mixer.music.load(file_name)

    # Play the mp3 file
    pygame.mixer.music.play()

    # Wait until the speech finishes playing
    while pygame.mixer.music.get_busy():
        pass

    # Quit Pygame
    pygame.quit()

def PlayAudio_playsound(file_name = 'output.wav'):
    #im pretty sure this needs a PATH to the file still work on this
    # Play the audio file
    playsound(file_name)

def PlayAudio_():
    #import sounddevice as sd
    #import soundfile as sf

    ## Load the audio file
    #data, fs = sf.read("audiofile.wav", dtype='float32')

    ## Play the audio file
    #sd.play(data, fs)
    #sd.wait()
    pass


def main():
    text = SpeechToText()
    print(text)
    TextToSpeech_aeiou(text)
    print("done")
    #PlayAudio_playsound()

#things to improve:
    #auto_PLayaudio
    #route_audio to input
    #special Button for me to press to start the recording
    #^^could just have a simple GUI that allows me to see what it said, and do that
    #fix the audio output for the normal computer(I kinda messed it up)

if __name__ == '__main__':
    main()