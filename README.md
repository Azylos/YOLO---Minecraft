# 🧠 Minecraft AI - Détection et Évasion Automatique

Ce projet utilise **YOLOv11** et **OpenCV** pour détecter des monstres dans Minecraft et automatiser des actions d'évitement en fonction des menaces rencontrées. Il détecte certains mob, et effectue des actions adaptées en réponse.

## 📌 Fonctionnalités

✅ **Détection d'ennemis** dans Minecraft en utilisant un modèle YOLO personnalisé.  
✅ **Évasion automatique** des Creepers en reculant et en sautant en cas d'obstacle.  
✅ **Réaction aux Zombies** en sautant uniquement lorsqu'ils sont visibles.  
✅ **Capture d'écran en temps réel** et affichage des FPS.  
---

## 🛠 Technologies utilisées

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) - Modèle de détection d'objets.
- [OpenCV](https://opencv.org/) - Traitement d'image.
- [mss](https://github.com/BoboTiG/python-mss) - Capture d'écran en temps réel.
- [pynput](https://pynput.readthedocs.io/en/latest/) - Automatisation du clavier.
- [Python](https://www.python.org/downloads/release/python-3119/) - Langage de programmation.
- [dataset minecraft](https://universe.roboflow.com/minecraft-object-detection/minecraft-mob-detection/dataset/10) - dataset mob minecraft.
***
## 🛠️ Prérequis
### **Installer les dépendances**
Assurez-vous d'avoir Python installé, puis exécutez :
```sh
pip install ultralytics opencv-python mss pynput numpy
```
***
## 📄 Documentation

- [YOLOv11](https://docs.ultralytics.com/fr/models/yolo11/)
- [pynput](https://www.youtube.com/watch?v=sJx_lFtrO3E)

***
![MobList](runs\detect\minecraft_detection\labels.jpg)