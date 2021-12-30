import cv2 as cv
import numpy as np
img = cv.imread('data/photo1.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
blank = np.zeros(img.shape, dtype='uint8')
blank2 = np.zeros(img.shape, dtype='uint8')
#convert to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey frame',gray)
#BGR tos HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv frame',hsv)
#BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab frame',lab)



#OpenCV use RGB the opposite of RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb frame',rgb)



# we can use the same logic to convert from LAB , HSV to BGR




cv.waitKey(0)

