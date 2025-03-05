import whisper
import sqlite3
import pyttsx3
import time
from database import Database

class VoiceRecognition:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)
        self.engine = pyttsx3.init()
        self.database = Database()

    def transcribe_audio(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result["text"]

    def store_voice_notes(self, name, notes):
        self.database.store_notes(name, notes)

    def prompt_user_for_notes(self):
        print("Please Say the name of the person: ")
        name_audio_path = "recorded_audio.wav"
        name = self.transcribe_audio(name_audio_path)
        print(f"Name recognized: {name}. Please add any notes or reminders: ")
        notes_audio_path = "recorded_audio.wav"
        notes = self.transcribe_audio(notes_audio_path)
        self.store_voice_notes(name, notes)
        self.engine.say(f"Notes for {name} have been saved!")
        self.engine.runAndWait()

    def run(self):
        while True:
            self.prompt_user_for_notes()
            time.sleep(5)

if __name__ == "__main__":
    voice_recognition = VoiceRecognition()
    voice_recognition.run()