import cv2 as cv
def rescaleFrame(frame,scale=0.25):
    #this work for :image, video live video
    width = int(frame.shape[1]*scale)
    height = int (frame.shape[0]* scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeResolution(videoCap,width,height):
    #work only for live video
    videoCap.set(3,width )
    videoCap.set(4,height)


#read video very and rescaled
capture = cv.VideoCapture(0) #the webcam
#opencv read file as image by image so we have to loop

while True:
    isTrue,frame = capture.read()
    cv.imshow('video',rescaleFrame(frame,scale=0.5))
    if cv.waitKey(20) & 0xFF == ord('d'): #letter d to exit
        break
capture.release()
cv.destroyAllWindows()
