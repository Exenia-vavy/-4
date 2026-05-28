import whisper
import sys
import subprocess

# 1. MODIFIE LE NOM DE LA VIDÉO ICI
video_source = r"C:\Users\Exenia\Desktop\videoss\movie2.mp4" 

# Chemins de sortie
son_wav = r"C:\Users\Exenia\Desktop\videoss\nouveau_son.wav"
texte_txt = r"C:\Users\Exenia\Documents\transcription_nouvelle.txt"

sys.stdout.reconfigure(encoding='utf-8')

# Étape A : Extraire le son de la nouvelle vidéo
print(f"Extraction du son de : {video_source}...")
subprocess.run(['ffmpeg', '-y', '-i', video_source, '-ar', '16000', '-ac', '1', son_wav], capture_output=True)

# Étape B : Reconnaissance
print("Transcription en cours...")
model = whisper.load_model("base")
result = model.transcribe(son_wav, language="en")

# Affichage et sauvegarde
print("-" * 30)
print(result["text"])
print("-" * 30)

with open(texte_txt, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Terminé ! Nouveau texte dans : {texte_txt}")
