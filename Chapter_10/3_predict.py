import os
from datetime import datetime
import cv2 as cv

names = {1: "Demming"}  # Update with your ID and name.

# Set up face detector path.
cascade_path = "C:/Python372/Lib/site-packages/cv2/data/"
face_detector = cv.CascadeClassifier(cascade_path +
                                     'haarcascade_frontalface_default.xml')

# Set up face recognizer and load trained data.
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('lbph_trainer.yml')

# Set up test data.
# Use tester folder for your face.
# Use demming_tester folder for pre-loaded images.

#test_path = './tester'
test_path = './demming_tester'
image_paths = [os.path.join(test_path, f) for f in os.listdir(test_path)]

# Loop through test images and predict faces.
for image in image_paths:
    predict_image = cv.imread(image, cv.IMREAD_GRAYSCALE)
    faces = face_detector.detectMultiScale(predict_image,
                                          scaleFactor=1.05,
                                          minNeighbors=5)
    for (x, y, w, h) in faces:
        print(f"\nAccess requested at {datetime.now()}.")
        face = cv.resize(predict_image[y:y + h, x:x + w], (100, 100))   
        predicted_id, dist = recognizer.predict(face)
        if predicted_id == 1 and dist <= 95:
            name = names[predicted_id]
            print("{} identified as {} with distance={}"
                  .format(image, name, round(dist, 1)))
            print(f"Access granted to {name} at {datetime.now()}.",
                  file=open('lab_access_log.txt', 'a'))
        else:
            name = 'unknown'
            print(f"{image} is {name}.")
        cv.rectangle(predict_image, (x, y), (x + w, y + h), 255, 2)
        cv.putText(predict_image, name, (x + 1, y + h -5),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1)
        cv.imshow('ID', predict_image)        
        cv.waitKey(2000)
        cv.destroyAllWindows()
