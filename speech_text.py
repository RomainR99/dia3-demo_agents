from config import WHISPER_MODEL


class speech_text:
    def __init__(self, groq_client):
        self.groq_client = groq_client

    def transcribe(self, audio_file):
        transcription = self.groq_client.audio.transcriptions.create(
            model=WHISPER_MODEL,
            file=(audio_file.name, audio_file.getvalue(), audio_file.type),
            language="fr",
        )
        return transcription.text
