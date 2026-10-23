from groq import Groq
import base64
from dotenv import load_dotenv
import os

from config import IMAGE_ONLY_QUESTION, TEXT_MODEL, VISION_MODEL
from speech_text import speech_text


class ConversationAgent:
    def __init__(self):
        load_dotenv()
        self.groq_client = Groq(api_key=os.environ["GROQ_KEY"])
        self.speech_text = speech_text(self.groq_client)
        self.conversation_history = [
                {
                    "role": "system",
                    "content": self.read_file(file_path="./context.txt")
                }
            ]


    @staticmethod
    def read_file(file_path):
        with open(file_path, "r") as file:
            return file.read()


    @staticmethod
    def encode_image(image):
        return base64.b64encode(image).decode("utf-8")


    def get_conversation_history(self):
        return self.conversation_history[1:]


    @staticmethod
    def build_content(text_interaction, image=None):
        if not image:
            return text_interaction

        content = []
        if text_interaction:
            content.append({
                "type": "text",
                "text": text_interaction,
            })
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{ConversationAgent.encode_image(image)}",
            },
        })
        return content


    def history_has_image(self):
        for message in self.conversation_history:
            content = message.get("content")
            if not isinstance(content, list):
                continue
            for part in content:
                if isinstance(part, dict) and part.get("type") == "image_url":
                    return True
        return False


    def update_conversation_history(self, role, text_interaction, image=None, speech=None):
        message = {
            "role": role,
            "content": self.build_content(text_interaction, image),
        }
        if speech is not None:
            message["speech"] = speech
        self.conversation_history.append(message)


    def transcribe(self, audio_file):
        return self.speech_text.transcribe(audio_file)


    def ask_llm(self, text_interaction, image=None):
        if image and not text_interaction:
            text_interaction = IMAGE_ONLY_QUESTION

        self.update_conversation_history(role="user", text_interaction=text_interaction, image=image)

        messages = [
            {"role": message["role"], "content": message["content"]}
            for message in self.conversation_history
        ]

        model = VISION_MODEL if self.history_has_image() else TEXT_MODEL
        response = self.groq_client.chat.completions.create(
            messages=messages,
            model=model,
            include_reasoning=False,
        ).choices[0].message.content

        self.update_conversation_history(role="assistant", text_interaction=response)
        return response


if __name__ == "__main__":
    question = input("Pose ta question :\n")
    response = ask_llm(question)
    print("\n")
    print(response)
