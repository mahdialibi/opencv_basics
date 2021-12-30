import cv2 as cv
import numpy as np
img = cv.imread('data/photo1.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
#convert to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey frame',gray)

#Blur
blured=cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT)
cv.imshow('blur frame',blured)

#edge  with canny algorithm
img2=cv.Canny(img,125,175)
cv.imshow('edges',img2)
#edges with sobel alg

# Sobel Edge Detection
sobelx = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv.imshow('Sobel X', sobelx)
cv.waitKey(0)
cv.imshow('Sobel Y', sobely)
cv.waitKey(0)
cv.imshow('Sobel X Y using Sobel() function', sobelxy)
cv.waitKey(0)
#dialate image 
dialated=cv.dilate(img,(10,3),iterations=50)
cv.imshow('dialated', dialated)
cv.waitKey(0)

#erode image 
eroded=cv.erode(dialated,(10,3),iterations=50)
cv.imshow('eroded', eroded)
cv.waitKey(0)

resized = cv.resize(img,(200,200),interpolation=cv.INTER_LINEAR)
cv.imshow('resize',resized)
cv.waitKey(0)