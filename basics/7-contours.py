import cv2 as cv
import numpy as np

img = cv.imread('data/photo1.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
blank = np.zeros(img.shape, dtype='uint8')
blank2 = np.zeros(img.shape, dtype='uint8')
#convert to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey frame',gray)
img2=cv.Canny(gray,125,175)
cv.imshow('edges',img2)
#other method to find the contours
#contours : list of contours found
#hierarchies : hiercharchie of the contours
contours,hierarchies =  cv.findContours(img2,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

#lets blur image and view contours
blured=cv.GaussianBlur(gray,(0,0),cv.BORDER_DEFAULT)
img3=cv.Canny(blured,125,175)
#hierarchies : hiercharchie of the contours
contours1,hierarchies1 =  cv.findContours(img3,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours (blank2,contours1,-1,(0,255,0),1)
cv.imshow('Contours2', blank)



cv.waitKey(0)