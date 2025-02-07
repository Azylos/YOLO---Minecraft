import os

base_path = "dataset"

# Vérification des dossiers
folders = ["train", "valid", "test"]
subfolders = ["images", "labels"]

for folder in folders:
    for sub in subfolders:
        path = os.path.join(base_path, folder, sub)
        if not os.path.exists(path):
            print(f"Erreur : Le dossier {path} est manquant !")
        else:
            print(f"OK : {path} existe")

# Vérification des correspondances images/annotations
for folder in folders:
    images = os.listdir(os.path.join(base_path, folder, "images"))
    labels = os.listdir(os.path.join(base_path, folder, "labels"))

    images = [img.replace(".jpg", ".txt") for img in images]  # Adapter si vos images sont en .png
    missing_labels = [img for img in images if img not in labels]

    if missing_labels:
        print(f"⚠️ Attention : Certaines images de {folder}/images/ n'ont pas de fichier .txt correspondant dans {folder}/labels/ :")
        print(missing_labels)
    else:
        print(f"✅ Toutes les images de {folder} ont des annotations correspondantes.")
