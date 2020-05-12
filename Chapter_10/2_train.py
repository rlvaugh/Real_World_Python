import os
import numpy as np
import cv2 as cv

# Set up path to OpenCV's Haar Cascades for face detection.
cascade_path = "C:/Python372/Lib/site-packages/cv2/data/"
face_detector = cv.CascadeClassifier(cascade_path +
                                    'haarcascade_frontalface_default.xml')

# Set up path to training images and prepare names/labels.
# For pre-loaded Demming images use demming_trainer folder.
# To use your own face use the trainer folder.

#train_path = './trainer'
train_path = './demming_trainer'  
image_paths = [os.path.join(train_path, f) for f in os.listdir(train_path)]
images, labels = [], []

# Extract face rectangles and assign numerical labels.
for image in image_paths:
    train_image = cv.imread(image, cv.IMREAD_GRAYSCALE)
    label = int(os.path.split(image)[-1].split('.')[1])
    name = os.path.split(image)[-1].split('.')[0]
    frame_num = os.path.split(image)[-1].split('.')[2]
    faces = face_detector.detectMultiScale(train_image)
    for (x, y, w, h) in faces:
        images.append(train_image[y:y + h, x:x + w])
        labels.append(label)
        print(f"Preparing training images for {name}.{label}.{frame_num}")
        cv.imshow("Training Image", train_image[y:y + h, x:x + w])
        cv.waitKey(50)    

cv.destroyAllWindows()

# Perform the tranining
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))
recognizer.write('lbph_trainer.yml')
print("Training complete. Exiting...")



