import pyaudio
import wave
import speech_recognition as sr
import requests


def SpeechToText():
    # Create an instance of the recognizer
    r = sr.Recognizer()

    # Listen to the audio from the microphone
    with sr.Microphone() as source:
        print("Say something...")
        #maybe I can make a button for this so it doesn't auto cut off
        audio = r.listen(source)

    print("Done Recording.")

    # Convert the audio to text
    text = r.recognize_google(audio)
    return text

def save_aeiou(input_string:str):
    import re

    # Define the regular expression pattern
    pattern = r"&"
    # Define the replacement string
    replacement = " and "

    # Use the sub() method of the re module to replace all instances of the pattern with the replacement string
    output_string = re.sub(pattern, replacement, input_string)

    return output_string

def TextToSpeech_aeiou(text:str,file_name:str = 'output.wav'):
    
    #NO SYMBOLS ALLOWED TEXT STRING

    text = save_aeiou(text)

    url = f'https://tts.cyzon.us/tts?text={text}'
    test = requests.get(url)
    response = test.content

    with open(file_name, mode='bw') as f:
        f.write(response)

    print("file made.")

class AudioFile:
    "This deals with playing the audio File"
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')

        #list of IDs:
            #inputs
        #1 Headset Microphone (HyperX Virt
        #2 Microphone (Virtual Desktop Aud
        #3 Microphone (Realtek Audio)
        #4 Stereo Mix (Realtek Audio)
        #5 CABLE Output (VB-Audio Virtual
            #outputs
        #6 Microsoft Sound Mapper - Output
        #7 Headset Earphone (HyperX Virtua
        #8 Speakers / Headphones (Realtek
        #9 CABLE Input (VB-Audio Virtual C

        self.output_device_id = 9
        self.input_device_id = 5

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output_device_index = self.output_device_id,
            input_device_index = self.input_device_id,
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

def playAudio_Pyaudio(audio_file:str):
    # Usage example for pyaudio
    print(f"playing {audio_file}")
    a = AudioFile(audio_file)
    a.play()
    a.close()
    print("done playing")

def put_test(inOut):

    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get(f'max{inOut}putChannels')) > 0:
            print(f"{inOut}put Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i),"\n")

def main():
    text = input("Wes Ban says: \t")
    TextToSpeech_aeiou(text)
    playAudio_Pyaudio()

if __name__ == "__main__":
    pass


#THINGS TO DO:
#verify this works
#make it so I can hear it as well, might need multi-threading and mess with pyaudio