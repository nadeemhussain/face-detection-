                                                    #it plays video as long it detects the face in front of the camera

import cv2
import utils
import time

   
    #detects the face in the image 
def update(image):
     
        faceClassifier = cv2.CascadeClassifier(
           'cascades/haarcascade_frontalface_alt.xml')
            
        
        if utils.isGray(image):
            image = cv2.equalizeHist(image)
        else:
            image = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
            cv2.equalizeHist(image, image)
        
        minSize = utils.widthHeightDividedBy(image, 8)
        
        faceRects = faceClassifier.detectMultiScale(
            image, 1.2, 2, cv2.cv.CV_HAAR_SCALE_IMAGE,
            minSize)
        
        if faceRects is not None:
            
            for faceRect in faceRects:
               return True


    
frame_video=cv2.VideoCapture('q.MP4')
frame_camera=cv2.VideoCapture(0)
cv2.namedWindow('video',1)

while True and cv2.waitKey(1) != 9:
    s_camera,image_camera=frame_camera.read()                           #read image from the source camera
    s_video,image_video=frame_video.read()                              #read imag form the video
    
    time.sleep(1/25)
    #e=FaceTracker()
    if not update(image_camera):
        print "noface"
        continue
    cv2.imshow('video',image_video)                   #display image to the source    
















