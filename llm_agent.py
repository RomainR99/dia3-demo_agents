from groq import Groq

from dotenv import load_dotenv
import os

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


    def get_conversation_history(self):
        return self.conversation_history[1: ]

    def update_conversation_history(self, role, content, speech=None):
        message = {
        "role": role,
        "content": content,
        }
        if speech is not None:
            message["speech"] = speech
        self.conversation_history.append(message) # le message contient le speech now



    def ask_llm(self, text_interaction):
        #pour la memoire de l'audio
        if text_interaction.audio is not None:
            question = self.speech_text.transcribe(text_interaction.audio)
        else:
            question = text_interaction.text

        self.update_conversation_history(role="user", content=question)

        messages = [
            {"role": message["role"], "content": message["content"]}
            for message in self.conversation_history
        ]

        response = self.groq_client.chat.completions.create(
            messages=messages,
            model="openai/gpt-oss-120b",
            include_reasoning=False,
        ).choices[0].message.content


        self.update_conversation_history(role="assistant", content=response)

   




























if __name__ == "__main__":
    question = input("Pose ta question :\n")
    response = ask_llm(question)
    print("\n")
    print(response)