import time
from voice_activation import VoiceActivation
from voice_recognition import VoiceRecognition

def main():
    voice_activation = VoiceActivation()
    voice_recognition = VoiceRecognition()
    while True:
        voice_activation.listen_for_wake_word()
        voice_recognition.prompt_user_for_notes()
        time.sleep(5)  # Wait for 5 seconds before next prompt

if __name__ == "__main__":
    main()