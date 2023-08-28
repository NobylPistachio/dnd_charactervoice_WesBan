from soundOutput import tts_using_aeiou,play_audio_to_them,AudioFile,play_audio_to_headphones
from threading import Thread

#this is a test for multithreading

def playAudio_Pyaudio3(audio_file_path,output=7):
    print(f"playing {audio_file_path}")
    a = AudioFile(audio_file_path,output)
    a.play()
    a.close()
    print("done playing")

def test(text):
    tts_using_aeiou(text)
    t1 = Thread(target = play_audio_to_them("output.wav"))
    t2 = Thread(target = play_audio_to_headphones("output.wav"))
    t1.start()
    t2.start()

t = input("what do you want to say?\n")
test(t)