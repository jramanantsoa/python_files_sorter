import os
from glob import glob
import shutil

chemin = os.path.join(os.getcwd(),"sources")

#dictionnaire avec les extensions et les dossiers associés
extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".mov": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents"}

#répertoire avec tous les fichiers
fichiers = glob(os.path.join(chemin,"*"))
for fichier in fichiers:
    extension = os.path.splitext(fichier)[-1]
    dossier = extensions.get(extension)
    #Si dossier de destination n'existe pas, on le crée
    if dossier:
        dossier_destination = os.path.join(chemin,dossier)
        os.makedirs(dossier_destination,exist_ok=True)
        shutil.move(fichier,dossier_destination)
