import os
import cv2 as cv
import numpy as np
import pathlib
current_path=str(pathlib.Path(__file__).parent.resolve())+"\\"

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = 'D:\Etudes\self-study\opencv_basics\data\\Faces\\train'
haar_cascade = cv.CascadeClassifier('advanced/face_detection_example/haar_cascade_default.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person) # each person will have his number as identification label

        
        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path) #just read the image
            if img_array is None:
                continue 
                
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY) #convert to gray
            
            #detecting the faces
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # region of interst: the face
                features.append(faces_roi)
                labels.append(label)

create_train()
features =np.array(features,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save(current_path+'face_trained.yml')
np.save(current_path+'feature.npy',features)
np.save(current_path+'labels.npy',labels)