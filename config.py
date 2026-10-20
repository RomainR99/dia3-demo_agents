TEXT_MODEL = "openai/gpt-oss-120b"
FAST_MODEL = "openai/gpt-oss-20b"
VISION_MODEL = "qwen/qwen3.8-27b"
WHISPER_MODEL = "whisper-large-v3-turbo"

LANGUAGE_INSTRUCTION = (
    "Tu réponds toujours en français. "
    "Tu n'écris jamais en anglais, même pour refuser."
)
VOICE_INSTRUCTION = (
    "L'utilisateur t'écoute et ne te lit pas. "
    "Chaque réplique fait entre 150 et 300 caractères, environ 2 à 4 phrases courtes. "
    "Cette longueur prime sur les autres consignes de longueur, y compris quand tu refuses. "
    "Si tu refuses, reste dans ton rôle, dis pourquoi, et propose autre chose. "
    "Pas de liste, pas de markdown, pas d'emoji."
)

PAGE_TITLE = "Jarvis"
APP_TITLE = "Barbe-Quasar"
CHAT_PLACEHOLDER = "Que veux tu moussaillon ?"
IMAGE_ONLY_QUESTION = "Que vois-tu sur cette image ?"