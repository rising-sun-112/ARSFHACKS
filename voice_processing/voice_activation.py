import pyaudio
import wave
import webrtcvad
import os

class VoiceActivation:
    def __init__(self, vad_aggressiveness=3, wake_word="Hey Xreal"):
        self.vad = webrtcvad.Vad(vad_aggressiveness)
        self.wake_word = wake_word
        self.chunk_size = 1024
        self.sample_rate = 16000
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=self.sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk_size)

    def is_speech(self, audio_chunk):
        return self.vad.is_speech(audio_chunk, self.sample_rate)

    def record_audio(self, duration=5):
        frames = []
        for _ in range(0, int(self.sample_rate / self.chunk_size * duration)):
            data = self.stream.read(self.chunk_size)
            frames.append(data)
        return frames

    def save_audio(self, frames, filename="recorded_audio.wav"):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()

    def listen_for_wake_word(self):
        print(f"Listening for wake word: {self.wake_word}")
        while True:
            data = self.stream.read(self.chunk_size)
            if self.is_speech(data):
                print("Speech detected, recording...")
                frames = self.record_audio()
                self.save_audio(frames)
                return

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

if __name__ == "__main__":
    voice_activation = VoiceActivation()
    voice_activation.listen_for_wake_word()
    voice_activation.close()