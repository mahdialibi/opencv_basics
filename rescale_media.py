import cv2 as cv
def rescaleFrame(frame,scale=0.25):
    #this work for :image, video live video
    width = int(frame.shape[1]*scale)
    height = int (frame.shape[0]* scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


img = cv.imread('data/photo1.jpg') #read the file as array
cv.imshow('photoframe',rescaleFrame(img)) # show the file in a window named "photoframe"
cv.waitKey(0) #wait for a key to be pushed 

#read video very and rescaled
capture = cv.VideoCapture('data/videofile.mp4') #the video file
#opencv read file as image by image so we have to loop
while True:
    isTrue,frame = capture.read()
    cv.imshow('video',rescaleFrame(frame,scale=0.10))
    if cv.waitKey(20) & 0xFF == ord('d'): #letter d to exit
        break
capture.release()
cv.destroyAllWindows()
