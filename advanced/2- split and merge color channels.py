import cv2 as cv
import numpy as np
img = cv.imread('data/photo1.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
#average blur
average = cv.blur(img,(7,7))
cv.imshow('averageblue',average)
#gaussian
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('gaussian',gauss)
#median
median = cv.medianBlur(img, 3)
cv.imshow('median',median)
#bilateral
bilateral = cv.bilateralFilter(img,100,15,150)
cv.imshow('bilateral',bilateral)

#





cv.waitKey(0)