# Rapport

## Pourquoi ne pas mettre `audio_file.wav` ?

`audio_file.wav` lirait un attribut nommé `wav` sur l'objet du micro. Cet attribut n'existe pas.

L'enregistrement Streamlit a trois informations séparées : `name` pour le nom du fichier, `getvalue()` pour les octets, et `type` pour `audio/wav`. Le `.wav` n'est pas une propriété. C'est l'extension déjà contenue dans `audio_file.name`, et le format déjà indiqué par `audio_file.type`.
