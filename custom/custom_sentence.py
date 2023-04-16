from SpeechToTextToSpeech import *

def main():
    text = input("What do you want to say? ")
    TextToSpeech_aeiou(text,'custom.mp3')
    print("done")

if __name__ == "__main__":
    main()