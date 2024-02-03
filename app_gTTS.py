from gtts import gTTS
import os
import re
import fitz  # PyMuPDF
import time
from pydub import AudioSegment

mypath = r"C:\Users\FiercePC\Desktop\IA\github\PDFtoMP3"

def extract_text_from_pdf_with_fitz(file_path, start_page, end_page):
    """Extrait le texte d'un PDF entre les pages spécifiées."""
    text = ''
    with fitz.open(file_path) as doc:
        start_page = max(0, start_page)
        end_page = min(len(doc) - 1, end_page)
        for page_num in range(start_page, end_page + 1):
            page = doc.load_page(page_num)
            text += page.get_text("text") + ' '
    return text.strip()

def apply_pronunciation_rules(text):
    """Applique des règles de prononciation personnalisées au texte."""
    replacement_rules = [
        (r'complexes', 'com-plex'),
        # Ajouter d'autres règles ici
    ]
    for pattern, replacement in replacement_rules:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text

def normalize_text(text):
    """Supprime les sauts de ligne inutiles et les espaces excessifs."""
    text = text.replace('\n', ' ')
    text = re.sub(' +', ' ', text)
    return text

def safe_tts_save(text, output_path, lang='fr', retries=5, delay=60):
    """Essaye de sauvegarder le TTS avec des réessais en cas d'erreur 429."""
    for attempt in range(retries):
        try:
            tts = gTTS(text=text, lang=lang)
            tts.save(output_path)
            print(f"Fichier MP3 généré : {output_path}")
            break  # Sortie de la boucle si réussi
        except Exception as e:
            print(f"Erreur rencontrée : {e}")
            if "429 (Too Many Requests)" in str(e) and attempt < retries - 1:
                print(f"Trop de requêtes, réessai dans {delay} secondes.")
                time.sleep(delay)  # Attend avant de réessayer
                delay *= 2  # Augmente le délai pour le prochain réessai
            else:
                raise  # Relève l'erreur si le nombre maximal de tentatives est atteint ou pour d'autres erreurs

def text_to_speech_segmented(text, output_file_name, lang='fr', segment_length=1000):
    """Convertit le texte en parole, sauvegarde en MP3 et fusionne les segments."""
    segments = [text[i:i+segment_length] for i in range(0, len(text), segment_length)]
    final_audio = AudioSegment.empty()
    for i, segment in enumerate(segments):
        segment_file_name = f"{output_file_name}_part_{i}.mp3"
        output_path = os.path.join(mypath, segment_file_name)
        safe_tts_save(segment, output_path, lang)
        segment_audio = AudioSegment.from_mp3(output_path)
        final_audio += segment_audio
        os.remove(output_path)  # Supprimer le fichier segment

    final_output_path = os.path.join(mypath, f"{output_file_name}_final.mp3")
    final_audio.export(final_output_path, format="mp3")
    print(f"Fichier MP3 final généré : {final_output_path}")

def main():
    """Fonction principale pour exécuter le processus de conversion."""
    start_time = time.time()

    pdf_files = [f for f in os.listdir(mypath) if f.endswith(".pdf")]
    if not pdf_files:
        print("Aucun fichier PDF trouvé.")
        return
    print("Fichiers PDF détectés :")
    for index, pdf_file in enumerate(pdf_files, start=1):
        print(f"{index}. {pdf_file}")

    try:
        choice = int(input("Entrez le numéro du fichier PDF à transformer en MP3 : ")) - 1
        pdf_file = pdf_files[choice]
        file_path = os.path.join(mypath, pdf_file)
        start_page = int(input("Entrez le numéro de la page de début : ")) - 1
        end_page = int(input("Entrez le numéro de la page de fin : ")) - 1
        text = extract_text_from_pdf_with_fitz(file_path, start_page, end_page)
        adjusted_text = apply_pronunciation_rules(text)
        output_file_name = os.path.splitext(pdf_file)[0]
        text_to_speech_segmented(adjusted_text, output_file_name, lang='fr')
    except ValueError as e:
        print(e)

    end_time = time.time()
    print(f"Temps de traitement total : {end_time - start_time:.2f} secondes.")

if __name__ == "__main__":
    main()
