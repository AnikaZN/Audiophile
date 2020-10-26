# Reference: https://www.codespeedy.com/get-voice-input-with-microphone-in-python-using-pyaudio-and-speechrecognition/

import speech_recognition as sr

# Print all the microphones connected to your machine, obtain device index
# print(sr.Microphone.list_microphone_names())
r = sr.Recognizer()
my_mic = sr.Microphone(device_index=1)

if __name__ == '__main__':
    signal = input('Are you ready? "y" for yes, "n" for no! (If you say yes, be ready to start talking!) ')

    if signal == "y":
        with my_mic as source:
            # Optional line to help with background noise
            # r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        print("You said: ", r.recognize_google(audio))
    else:
        print("See you later!")
