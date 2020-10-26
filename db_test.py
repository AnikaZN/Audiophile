'''
References:
https://pypi.org/project/SpeechRecognition/
https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py
'''

import speech_recognition as sr

r = sr.Recognizer()
my_mic = sr.Microphone(device_index=1)

if __name__ == '__main__':
    signal = input('Are you ready? "y" for yes, "n" for no! (If you say yes, be ready to start talking!) ')

    if signal == "y":
        with my_mic as source:
            audio = r.listen(source)
            text = r.recognize_google(audio)

        print("You said: ", text)

        # Write audio to a WAV file
        with open(f"clips/{text[:20]}.wav", "wb") as f:
            f.write(audio.get_wav_data())

        audio_file = f"clips/{text[:20]}.wav"
        print(audio_file)

        # Store all of it to a database

    else:
        print("See you later!")
