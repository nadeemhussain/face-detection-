# -*- coding: utf-8 -*-
#press tab to exit
"""
Created on Tue Jun 11 12:53:09 2013

@author: andy
"""
import trackers 
import cv2

def outlineRect(image, rect, color):
    if rect is None:
        return
    x, y, w, h = rect
    cv2.rectangle(image, (x, y), (x+w, y+h), color)

frame=cv2.VideoCapture(0)
cv2.namedWindow('a',1)
image=cv2.imread('i.jpg')
s,x=frame.read()    
while True and cv2.waitKey(1) != 9 :
   s,x=frame.read()
   e=trackers.FaceTracker()
   e.update(x)
   e.drawDebugRects(x)
   #outlineRect(x,[0,0,400,400],1)
   cv2.imshow('a',x)
