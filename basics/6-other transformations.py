import cv2 as cv
import numpy as np
img = cv.imread('data/photo2.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"


def translate(img,x,y):
    """translate the image by x, y
     x < 0 left 
     y < 0 up
     x > 0 right
     y > 0 down  """
    transMatrix=np.float32([[1,0,x],[0,1,y]])
    # | 1, 0, x |
    # | 0, 1, y |
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMatrix,dimensions)

def rotate(img,angle,rotationPoint=None):
    (height,width)=img.shape[:2]
    if rotationPoint is None:
        rotationPoint=(width//2,height//2)
    rotationMatrix=cv.getRotationMatrix2D(rotationPoint,angle,1.0)
    dimensions=(height,width)
    return cv.warpAffine(img,rotationMatrix,dimensions)


translated=translate(img,-100,50)
cv.imshow('translate',translated)

rotated = rotate(img,-45,(5,5))
cv.imshow('rotated',rotated)

#Flipping
flipped = cv.flip(img,1) #(0 , 1 , -1)
cv.imshow('flipped',flipped)
cv.waitKey(0) #wait for a key to be pushed 