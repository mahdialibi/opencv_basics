import cv2 as cv
import numpy as np
blank = np.zeros((400,400), dtype='uint8')
# a solid color rectangle and circle
rectangle = cv.rectangle(blank.copy(),(30,30),(250,250),255,-1)
circle = cv.circle(blank.copy(),(200,200),150,255,-1)
cv.imshow('rectangle',rectangle)
cv.imshow ('circle',circle)

#bitwise
bitwise_and = cv.bitwise_and(rectangle,circle)
bitwise_or=cv.bitwise_or(rectangle,circle)
bitwise_xor= cv.bitwise_xor(rectangle,circle)

cv.imshow('and',bitwise_and)
cv.imshow('or',bitwise_or)
cv.imshow('xor',bitwise_xor)



cv.waitKey(0)