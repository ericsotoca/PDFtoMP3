```markdown
# Conversion de PDF en MP3

## Table des matières
- [Description](#description)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités](#fonctionnalités)
- [Contributions](#contributions)
- [Support](#support)
- [Licence](#licence)

## Description
Ce projet propose deux scripts pour convertir des fichiers PDF en fichiers audio MP3.
En utilisant soit Google Text-to-Speech (`app_gTTS.py`) pour une conversion en ligne, soit `pyttsx3` (`app_pyttsx3.py`)
pour une conversion hors ligne. Les scripts exploitent `PyMuPDF` pour l'extraction de texte et `pydub` pour la manipulation audio.

## Prérequis
- Python 3.6 ou supérieur
- Système d'exploitation : Windows, Linux, ou macOS

## Installation
Clonez d'abord le dépôt :
git clone https://github.com/votre_nom_utilisateur/votre_depôt.git
cd votre_depôt

Installez ensuite les dépendances nécessaires :
pip install -r requirements.txt

## Utilisation
# Pour le script gTTS
python app_gTTS.py /chemin/vers/le/pdf page_de_début page_de_fin

# Pour le script pyttsx3
python app_pyttsx3.py /chemin/vers/le/pdf page_de_début page_de_fin
Remplacez les placeholders par vos propres valeurs.

## Fonctionnalités
- **app_gTTS.py** : Convertit du texte extrait de PDF en audio en utilisant Google Text-to-Speech.
- **app_pyttsx3.py** : Offre une alternative hors ligne pour la conversion de texte en parole avec `pyttsx3`.

## Contributions
Pour contribuer au projet, veuillez consulter notre guide de contribution dans `CONTRIBUTING.md`.
Nous accueillons les pull requests, les corrections de bugs, et les suggestions d'améliorations.

## Support
Si vous avez des questions ou rencontrez des problèmes, veuillez ouvrir une issue sur GitHub.

## Licence
Ce projet est sous licence [MIT](LICENSE). Consultez le fichier `LICENSE` pour plus de détails.
