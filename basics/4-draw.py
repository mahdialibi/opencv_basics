import cv2 as cv
import numpy as np
img = cv.imread('data/photo1.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
#blank image
blank = np.zeros((600,600,3),dtype="uint8") #blank image = arrau of 0 , 3 is for the 3 colors of RGB
cv.imshow('blankframe',blank)
#adding color to the image
colored =np.copy(blank) #copy the array /image
colored[200:300,300:400]= 0,200,255 #applyiong some color 
cv.imshow('color frame',colored)
#draw ractangle 
cv.rectangle(blank,(0,0),(250,500),(0,255,220),thickness=3)
cv.imshow('rectangle frame',blank)
#draw filled rectangle
cv.rectangle(blank,(0,0),(245,510),(0,255,0),thickness=-1)
cv.imshow('rectangle 2 frame',blank)
#draw circle
cv.circle(blank,(250,250),40,(0,255,110),thickness=-1)
cv.imshow('rectangle 3 frame',blank)

#draw a line

cv.line(blank,(250,250),(40,255),(0,0,255),thickness=3)
cv.imshow('rectangle 4 frame',blank)

#wrtie a text
cv.putText(blank,'Hi I am a text',(200,200),cv.FONT_HERSHEY_SCRIPT_COMPLEX,2.0,(0,200,255),5)
cv.imshow('text',blank)



cv.waitKey(0) #wait for a key to be pushed 
