import os
import time
from datetime import datetime
from playsound import playsound
import pyttsx3
import cv2 as cv

# Set up warning audio.
engine = pyttsx3.init()
engine.setProperty('rate', 145)  # Fast but clear.
engine.setProperty('volume', 1.0)  # Max is 1.0.

# Set up audio files.
root_dir = os.path.abspath('.')
gunfire_path = os.path.join(root_dir, 'gunfire.wav')
tone_path = os.path.join(root_dir, 'tone.wav')

# Set up Haar cascades for face detection.
path = "C:/Python372/Lib/site-packages/cv2/data/"
face_cascade = cv.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(path + 'haarcascade_eye.xml')

# Set up corridor images.
os.chdir('corridor_5')
contents = sorted(os.listdir())

# Detect faces and fire or disable gun.
for image in contents:
    print(f"\nMotion detected...{datetime.now()}")
    discharge_weapon = True
    engine.say("You have entered an active fire zone. \
               Stop and face the gun immediately. \
               When you hear the tone, you  have 5 seconds to pass.")
    engine.runAndWait()
    time.sleep(3)
    
    img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE)
    height, width = img_gray.shape
    cv.imshow(f'Motion detected {image}', img_gray)
    cv.waitKey(2000)
    cv.destroyWindow(f'Motion detected {image}')

    # Find face rectangles.
    face_rect_list = []  
    face_rect_list.append(face_cascade.detectMultiScale(image=img_gray,
                                                        scaleFactor=1.1,
                                                        minNeighbors=5))
    print(f"Searching {image} for eyes.")
    for rect in face_rect_list:
        for (x, y, w, h) in rect:
            rect_4_eyes = img_gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(image=rect_4_eyes,
                                                scaleFactor=1.05,
                                                minNeighbors=2)
            for (xe, ye, we, he) in eyes:
                print("Eye detected.")
                center = (int(xe + 0.5 * we), int(ye + 0.5 * he))
                radius = int((we + he) / 3)
                cv.circle(rect_4_eyes, center, radius, 255, 2)
                cv.rectangle(img_gray, (x, y), (x+w, y+h), (255, 255, 255), 2)
                discharge_weapon = False
                break
            
    if discharge_weapon == False:
        playsound(tone_path, block=False)
        cv.imshow('Detected Faces', img_gray)
        cv.waitKey(2000)
        cv.destroyWindow('Detected Faces')
        time.sleep(5)

    else:
        print(f"No face in {image}. Discharging weapon!")
        cv.putText(img_gray, 'FIRE!', (int(width / 2) - 20, int(height / 2)),
                                       cv.FONT_HERSHEY_PLAIN, 3, 255, 3)
        playsound(gunfire_path, block=False)
        cv.imshow('Mutant', img_gray)
        cv.waitKey(2000)
        cv.destroyWindow('Mutant')
        time.sleep(3)  # To delay loading next image...

engine.stop()  # Optional.
