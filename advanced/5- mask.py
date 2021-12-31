import cv2 as cv
import numpy as np
img = cv.imread('data/photo1.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
blank = np.zeros(img.shape[:2], dtype='uint8')
for i in range (3):
    rectangle_mask = cv.rectangle(blank.copy(),(30+100*i,30),(250+100*i,250+25*i),255,-1)
    masked_img=cv.bitwise_and(img,img,mask=rectangle_mask)
    cv.imshow('masked'+str(i),masked_img)




cv.waitKey(0)