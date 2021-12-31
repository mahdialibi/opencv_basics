import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('data/photo4.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_hist=cv.calcHist([gray],[0],None,[255],[0,256])

plt.figure(1)
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('# pixels')
plt.plot(gray_hist)
plt.xlim([0,255])
plt.show()
#color histogram
plt.figure(2)
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('# pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)