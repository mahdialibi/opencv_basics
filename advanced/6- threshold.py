import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('data/text.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple thresholde
threshold,thresh =cv.threshold(gray,200,255,cv.THRESH_BINARY)
cv.imshow("img thresh",thresh)
# adaptive threshold
adaptive_threshold=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 11,2)
cv.imshow("img adaptative thresh",adaptive_threshold)
#preprocessing with blur
blured = cv.medianBlur(gray, 3)
adaptive_threshold_blured=cv.adaptiveThreshold(blured,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 11,2)
cv.imshow('preprocessed ',adaptive_threshold_blured)
# we can see that we can use this for preprocessing and detecting caracters in image

cv.waitKey(0)