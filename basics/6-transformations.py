import cv2 as cv
img = cv.imread('data/photo3.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
cv.waitKey(0) #wait for a key to be pushed 
