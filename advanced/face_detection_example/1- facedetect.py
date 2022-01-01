import cv2 as cv
img= cv.imread('data/face.jpg')
cv.imshow('person', img)

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar= cv.CascadeClassifier()
haar.load('advanced/face_detection_example/haar_cascade_default.xml')
#haar_cascade=cv.CascadeClassifier('haar_cascade_default.xml')
faces_rect =haar.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("detect",img)
cv.waitKey(0)