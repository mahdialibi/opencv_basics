import cv2 as cv
import numpy as np
img = cv.imread('data/photo4.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
#splitting image to 3 images by color channel
#image is always a numpy array
b,g,r = cv.split(img)

cv.imshow('blue',b)
cv.imshow('red',r)
cv.imshow('green',g)

#merging the three channels to get original color
#try to inverse the colors to get fancy image
#merged = cv.merge([g,r,b]) #fancy image
merged = cv.merge([b,g,r]) #original image
cv.imshow('merged',merged)

cv.waitKey(0)