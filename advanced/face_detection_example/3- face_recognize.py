#haar is not the best recognizer

from typing import TYPE_CHECKING
import cv2 as cv
import numpy as np
import pathlib
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
current_path=str(pathlib.Path(__file__).parent.resolve())+"\\"
DIR = 'D:\Etudes\self-study\opencv_basics\data\\Faces\\val'
haar= cv.CascadeClassifier('advanced/face_detection_example/haar_cascade_default.xml')
feature=np.load(current_path+'feature.npy',allow_pickle=True)
labels= np.load(current_path+'labels.npy')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(current_path+'face_trained.yml')
img= cv.imread(DIR+'\\ben_afflek\\2.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces_rect =haar.detectMultiScale(gray, 1.3, 1)
for (x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+h]
    label,confidence = face_recognizer.predict(faces_roi)
    print (f'label={people[label]} with a confidence oh {confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)


cv.imshow("detect",img)
cv.waitKey(0)