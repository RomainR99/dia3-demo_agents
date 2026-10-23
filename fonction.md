# Fonctionnalités

À faire : 12. Faites : 1. Total : 13.

Commits à faire : 12. Un commit par fonctionnalité encore à coder, dans l'ordre de priorité ci-dessous.

Emery : 4 fonctionnalités, 15 def, 19 tests. Dorian : 4 fonctionnalités, 17 def, 20 tests. Romain : 4 fonctionnalités, 5 def, 8 tests.

Def à avoir : 37. Def faites : 15. Total : 52.

Le code actuel est `llm_agent.py`, `speech_text.py`, `user_interface.py` et `config.py`. Pas de comptes, pas de flux RSS, pas de Gmail.

## Def à avoir

| Priorité | Classe | Def | Qui | Noms |
| --- | --- | --- | --- | --- |
| 1 | `User` | 3 | Emery | `create_user`, `authenticate`, `get_user_persona` |
| 2 | `Message` | 2 | Emery | `load_messages`, `add_message` |
| 3 | `Feed` | 4 | Emery | `list_feeds`, `set_feed_active`, `fetch_entries`, `refresh_user` |
| 4 | `Article` | 2 | Emery | `recent_articles`, `digest_for` |
| 5 | `Mailbox` | 8 | Dorian | `save_mailbox`, `disconnect_mailbox`, `get_mailbox_credentials`, `connect_mailbox`, `fetch_newsletters`, `matches_theme`, `refresh_mailbox`, `delete_mail_articles` |
| 6 | `ConversationAgent` | 4 | Dorian | `speak`, `text_for_speech`, `first_spoken_sentence`, `split_for_speech` |
| 6 | `ConversationAgent` | 1 | Romain | `prepare_image` |
| 7 | `UserInterface` | 2 | Emery | `require_user`, `show_veille` |
| 7 | `UserInterface` | 3 | Dorian | `_show_gmail`, `_handle_turn`, `stream_voice_answer` |
| 8 | `Sujet` | 2 | Emery | `propose_topics`, `fetch_trends` |
| 9 | `Post` | 2 | Dorian | `draft_post`, `save_post_edit` |
| 10 | `Video` | 1 | Romain | `build_video` |
| 11 | `DiscordServeur` | 1 | Romain | `send_discord` |
| 12 | `CanvaDesign` | 2 | Romain | `create_canva`, `refresh_canva` |

## Def faites

3 classes. 15 def présentes dans le code.

| Priorité | Classe | Def | Noms |
| --- | --- | --- | --- |
| 1 | `ConversationAgent` | 8 | `ask_llm`, `transcribe`, `read_file`, `encode_image`, `get_conversation_history`, `build_content`, `history_has_image`, `update_conversation_history` |
| 2 | `speech_text` | 1 | `transcribe` |
| 3 | `UserInterface` | 6 | `run`, `get_persistant_conversation_agent`, `show_discussion_history`, `display_message`, `display_image`, `show_message` |

## À faire

| Priorité | Qui | Fonctionnalité | Commit |
| --- | --- | --- | --- |
| 1 | Emery | Comptes et séparation : création, persona techno ou finance, mot de passe, historique propre à chaque compte. | 1 |
| 2 | Emery | Flux RSS : lecture, rafraîchissement des 8 flux du thème, extrait de titres et de liens pour l'agent. | 1 |
| 3 | Dorian | Gmail et thème : connexion, mois précédent, newsletters retenues selon le persona, les autres laissées de côté. | 1 |
| 4 | Dorian | Réponse vocale : lire la réponse en français, avec la découpe du texte pour la voix. | 1 |
| 5 | Emery | Proposer des sujets selon le persona, à partir des flux RSS et des newsletters retenues. | 1 |
| 6 | Emery | Ajouter les tendances Twitter du thème, sans bloquer les sujets si Twitter ne répond pas. | 1 |
| 7 | Dorian | Rédiger un texte parlable de 2 à 3 minutes sur le sujet choisi. | 1 |
| 8 | Dorian | Laisser modifier le texte, et n'envoyer en vidéo que la version validée. | 1 |
| 9 | Romain | Monter la vidéo : images, voix et sous-titres alignés sur le texte validé. | 1 |
| 10 | Romain | Envoyer la vidéo sur le serveur Discord du compte. Si le fichier est trop lourd, envoyer un lien. | 1 |
| 11 | Romain | Créer le design Canva et joindre le lien d'édition au message Discord. | 1 |
| 12 | Romain | Reprendre un Canva modifié : même voix, nouveaux visuels, sous-titres. Refuser un lien collé sans identifiant de design. | 1 |

## Faites

| Priorité | Fonctionnalité |
| --- | --- |
| 1 | Dialogue : question, image et transcription. La veille du compte n'est pas encore dans le contexte. |
