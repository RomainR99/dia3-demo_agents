import base64

import streamlit as st
from llm_agent import ConversationAgent
from config import (
	APP_TITLE,
	CHAT_PLACEHOLDER,
	PAGE_TITLE,
)


class UserInterface:
	def __init__(self):
		st.set_page_config(page_title=APP_TITLE)
		st.title(PAGE_TITLE)
		self.conversation_agent_object = self.get_persistant_conversation_agent()


	def get_persistant_conversation_agent(self):
		if "conversation_agent_object" not in st.session_state:
			st.session_state.conversation_agent_object = ConversationAgent()

		return st.session_state.conversation_agent_object


	@staticmethod
	def display_image(base64_image):
		image_bytes = base64.b64decode(base64_image.split(",", 1)[1])
		st.image(image_bytes, width=150)


	@staticmethod
	def display_message(message):
		with st.chat_message(message["role"]):
			content = message["content"]
			if isinstance(content, list):
				for part in content:
					if part["type"] == "text":
						st.markdown(part["text"])
					elif part["type"] == "image_url":
						UserInterface.display_image(part["image_url"]["url"])
			else:
				st.markdown(content)
			UserInterface.show_message(message)


	@staticmethod
	def show_message(message):
		if message.get("speech"):
			st.audio(message["speech"], format="audio/wav")


	def show_discussion_history(self):
		for message in self.conversation_agent_object.get_conversation_history():
			self.display_message(message)


	def run(self):
		user_interaction = st.chat_input(
			CHAT_PLACEHOLDER,
			accept_file=True,
			accept_audio=True,
			file_type=["jpg", "jpeg", "png"],
		)

		if not user_interaction:
			return

		if user_interaction.audio:
			text_interaction = self.conversation_agent_object.transcribe(user_interaction.audio)
		else:
			text_interaction = user_interaction.text

		image = user_interaction.files[0].getvalue() if user_interaction.files else None

		if text_interaction or image:
			self.conversation_agent_object.ask_llm(text_interaction, image)
			self.show_discussion_history()


if __name__ == "__main__":
	user_interface_object = UserInterface()
	user_interface_object.run()
