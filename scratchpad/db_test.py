'''
References:
https://pypi.org/project/SpeechRecognition/
https://github.com/Uberi/speech_recognition/blob/master/examples/write_audio.py
'''

import speech_recognition as sr
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)

def refresh():
    DB.drop_all()
    DB.create_all()
    DB.session.commit()
    return "Refreshed! Please record your audio again."

r = sr.Recognizer()
my_mic = sr.Microphone(device_index=1)

class Audio(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    file_loc = DB.Column(DB.String(50))
    full_text = DB.Column(DB.String(200))

    def __repr__(self):
        return f'The file located at {self.file_loc} says the following: {self.full_text}'

def record():
    signal = input('Are you ready? "y" for yes, "n" for no! (If you say yes, be ready to start talking!) ')

    if signal == "y":
        with my_mic as source:
            audio = r.listen(source)
            text = r.recognize_google(audio)

        print("You said: ", text)

        # Write audio to a WAV file
        with open(f"./clips/{text[:20]}.wav", "wb") as f:
            f.write(audio.get_wav_data())

        audio_file = f"clips/{text[:20]}.wav"

        # Store all of it to a database
        try:
            audio_inst = Audio(file_loc=audio_file, full_text=text)
            DB.session.add(audio_inst)
            DB.session.commit()
            print('Added to the database!')
        except:
            print(refresh())

    else:
        print("See you later!")

if __name__ == '__main__':
    record()
