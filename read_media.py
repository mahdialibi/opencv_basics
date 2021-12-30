import cv2 as cv
img = cv.imread('data/photo1.jpg') #read the file as array
cv.imshow('photoframe',img) # show the file in a window named "photoframe"
cv.waitKey(0) #wait for a key to be pushed 

#read video very simple example
capture = cv.VideoCapture('data/videofile.mp4') #the video file
#opencv read file as image by image so we have to loop
while True:
    isTrue,frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF == ord('d'): #letter d to exit
        break
capture.release()
cv.destroyAllWindows()


