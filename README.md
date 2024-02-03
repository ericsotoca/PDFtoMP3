# Conversion de PDF en MP3

## Description
Ce projet contient deux scripts permettant de convertir des fichiers PDF en fichiers audio MP3. `app_gTTS.py` utilise Google Text-to-Speech pour une conversion en ligne, tandis que `app_pyttsx3.py` utilise `pyttsx3` pour une conversion hors ligne. Les deux méthodes utilisent `PyMuPDF` pour extraire le texte des PDF et `pydub` pour manipuler les fichiers audio.

## Installation
Pour installer les dépendances nécessaires, exécutez la commande suivante :
```bash
pip install -r requirements.txt

## Utilisation
Pour utiliser le script gTTS : python app_gTTS.py <chemin_vers_pdf> <page_début> <page_fin>
Pour utiliser le script pyttsx3 : python app_pyttsx3.py <chemin_vers_pdf> <page_début> <page_fin>
Remplacez <chemin_vers_pdf>, <page_début>, et <page_fin> par vos propres valeurs.

## Contributions
Les contributions à ce projet sont les bienvenues. N'hésitez pas à proposer des améliorations ou à signaler des problèmes via les issues GitHub.

## Licence
Ce projet est distribué sous une licence libre. Vous êtes libres de l'utiliser, de le modifier et de le distribuer.
