import pyaudio
import wave

from SpeechToTextToSpeech import main as sttts
from SpeechToTextToSpeech import tts_using_aeiou,tts_bot


from threading import Thread


class AudioFile:
    chunk = 1024

    def __init__(self, file, output):
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

        self.output_device_id = output
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

def play_audio_to_them(audio_file_path,output=9):
    # Usage example for pyaudio
    print(f"playing {audio_file_path} for them")
    a = AudioFile(audio_file_path,output)
    a.play()
    a.close()
    print("done playing for them")

def play_audio_to_headphones(audio_file_path):
        # Usage example for pyaudio
    print(f"playing {audio_file_path} for me")
    a = AudioFile(audio_file_path,7)
    a.play()
    a.close()
    print("done playing for me")


def main():
    sttts()
    play_audio_to_them("output.wav")


def put_test(inOut, printInfo:bool=True) -> list:
    "inOut can take 'In' or 'Out'"
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    devices = []
    if printInfo:
        for i in range(numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get(f'max{inOut}putChannels')) > 0:
                print(f"{inOut}put Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i),"\n")

    return 

def give_IO():
    ...


def tts_b(text):
    tts_using_aeiou(text)
    play_audio_to_headphones("output.wav")

def tts_a(text):
    tts_bot(text)
    play_audio_to_them("output.wav")

def tts_test(text):
    tts_using_aeiou(text)
    Thread(target=play_audio_to_them("output.wav")).start()
    Thread(target=play_audio_to_headphones("output.wav")).start()

if __name__ == "__main__":
    while True:
        text = input("Wes Ban says:\t")
        tts_b(text)
    # main()
#playAudio_Pyaudio("output.wav")
#put_test("In")