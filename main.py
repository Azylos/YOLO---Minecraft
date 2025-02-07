from ultralytics import YOLO
import mss
import numpy as np
import cv2
from pynput.keyboard import Key, Controller
import time

# Charger le modèle YOLO personnalisé
model = YOLO("runs\\detect\\minecraft_detection\\weights\\best.pt")

# Définir la zone de capture
monitor = {"top": 100, "left": 200, "width": 1280, "height": 720}
keyboard = Controller()

# Variables d'état
last_creeper_time = 0
last_zombie_time = 0
zombie_detected = False
creeper_detected = False

def capture_screen():
    """ Capture l'écran avec mss et le convertit pour OpenCV. """
    with mss.mss() as sct:
        frame = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame

while True:
    start_time = time.time()

    # Capture et analyse de l'écran
    frame = capture_screen()
    results = model(frame)

    # Réinitialisation des états de détection
    current_zombie_detected = False
    current_creeper_detected = False

    # Détection et gestion des entités
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = result.names[int(box.cls[0])]
            conf = box.conf[0].item()

            if conf > 0.5:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Gestion des Zombies
                if label == "zombie":
                    current_zombie_detected = True  # On note qu'un zombie est vu
                    last_zombie_time = time.time()  # On enregistre le dernier moment où on l'a vu
                    print("ATTENTION ZOMBIE !")
                    keyboard.press(Key.space)  # Sauter pour éviter l'attaque
                    time.sleep(0.2)  # Petite pause pour éviter un spam
                    keyboard.release(Key.space)

                # Gestion des Creepers
                elif label == "creeper" and conf > 0.6:
                    current_creeper_detected = True
                    last_creeper_time = time.time()
                    print("FUYEZ, CREEPER !")
                    
                    # On recule
                    keyboard.press("s")
                    time.sleep(0.5)  # Petite pause
                    keyboard.release("s")

                    # Vérifier si on est bloqué par un obstacle
                    time.sleep(0.2)  # Temps pour voir si on avance
                    keyboard.press("s")
                    keyboard.press(Key.space)  # Sauter pour éviter l'obstacle
                    time.sleep(0.2)
                    keyboard.release(Key.space)
                    keyboard.release("s")

                # Définir la couleur de danger
                color = (0, 0, 255) if label in ["zombie", "creeper"] else (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    # **Arrêter de sauter si le zombie n'est plus visible**
    if zombie_detected and not current_zombie_detected and time.time() - last_zombie_time > 1:
        print("Plus de zombie détecté, arrêt du saut")
        zombie_detected = False  # Désactivation du saut

    # **Continuer à sauter et reculer si un Creeper est proche**
    if creeper_detected and not current_creeper_detected and time.time() - last_creeper_time < 2:
        print("Vérification Creeper : encore en fuite !")
        keyboard.press("s")
        time.sleep(0.5)
        keyboard.release("s")

    # Mise à jour des états de détection
    zombie_detected = current_zombie_detected
    creeper_detected = current_creeper_detected

    # Affichage des FPS
    end_time = time.time()
    fps = 1 / (end_time - start_time)
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Affichage en temps réel
    cv2.imshow("Minecraft AI", frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
