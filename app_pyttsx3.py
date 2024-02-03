import fitz  # PyMuPDF
import os
import pyttsx3
from pydub import AudioSegment
import time  # Importe le module time pour le chronomètre

# Chemin d'accès au dossier contenant les fichiers PDF
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

def preprocess_text(text):
    """Prétraite le texte pour remplacer les sauts de ligne par des espaces."""
    text = text.replace('\n', ' ')
    return text

def text_to_speech_with_pyttsx3(text, output_file_name):
    """Convertit le texte en parole, avec prétraitement pour éviter les arrêts à chaque fin de ligne."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    processed_text = preprocess_text(text)
    temp_file = os.path.join(mypath, f"{output_file_name}_temp.wav")
    engine.save_to_file(processed_text, temp_file)
    engine.runAndWait()  # Attend que l'enregistrement soit terminé
    sound = AudioSegment.from_wav(temp_file)
    final_output_path = os.path.join(mypath, f"{output_file_name}.mp3")
    sound.export(final_output_path, format="mp3")
    os.remove(temp_file)
    return final_output_path

def jouer_alerte_fin_de_traitement():
    """Joue une alerte sonore pour indiquer la fin du traitement."""
    engine = pyttsx3.init()
    message_alerte = "Génération terminée."
    engine.say(message_alerte)
    engine.runAndWait()

def main():
    start_time = time.time()  # Début du chronomètre

    pdf_files = [f for f in os.listdir(mypath) if f.endswith(".pdf")]
    if not pdf_files:
        print("Aucun fichier PDF trouvé.")
        return

    print("Fichiers PDF détectés :")
    for index, pdf_file in enumerate(pdf_files, start=1):
        print(f"{index}. {pdf_file}")

    try:
        choice = int(input("Entrez le numéro du fichier PDF à transformer en MP3 : ")) - 1
        if not 0 <= choice < len(pdf_files):
            raise ValueError("Choix invalide.")

        pdf_file = pdf_files[choice]
        file_path = os.path.join(mypath, pdf_file)
        start_page = int(input("Entrez le numéro de la page de début : ")) - 1
        end_page = int(input("Entrez le numéro de la page de fin : ")) - 1
        text = extract_text_from_pdf_with_fitz(file_path, start_page, end_page)
        output_file_name = os.path.splitext(pdf_file)[0]
        final_output_path = text_to_speech_with_pyttsx3(text, output_file_name)
        print(f"Fichier MP3 généré : {final_output_path}")
    except ValueError as e:
        print(e)

    jouer_alerte_fin_de_traitement()

    end_time = time.time()  # Fin du chronomètre
    total_time = end_time - start_time  # Calcul de la durée totale
    print(f"Durée totale du processus : {total_time:.2f} secondes.")

if __name__ == "__main__":
    main()
