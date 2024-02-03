# Conversion de PDF en MP3

## Description
Ce projet contient deux scripts permettant de convertir des fichiers PDF en fichiers audio MP3. `app_gTTS.py` utilise Google Text-to-Speech pour une conversion en ligne, tandis que `app_pyttsx3.py` utilise `pyttsx3` pour une conversion hors ligne. Les deux méthodes utilisent `PyMuPDF` pour extraire le texte des PDF et `pydub` pour manipuler les fichiers audio.

## Installation
Pour installer les dépendances nécessaires, exécutez la commande suivante :
```bash
pip install -r requirements.txt
