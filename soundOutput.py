import pyaudio
import wave

from SpeechToTextToSpeech import main as sttts
from SpeechToTextToSpeech import tts_boi

class AudioFile:
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

def playAudio_Pyaudio(audio_file):
    # Usage example for pyaudio
    print(f"playing {audio_file}")
    a = AudioFile(audio_file)
    a.play()
    a.close()
    print("done playing")

def main():
    sttts()
    playAudio_Pyaudio("output.wav")


def put_test(inOut):

    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get(f'max{inOut}putChannels')) > 0:
            print(f"{inOut}put Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i),"\n")

def tts_b(text):
    tts_boi(text)
    playAudio_Pyaudio("output.wav")

if __name__ == "__main__":
    while True:
        text = input("Wes Ban says:\t")
        tts_b(text)
    # main()
#playAudio_Pyaudio("output.wav")
#put_test("In")