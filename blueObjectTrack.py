import cv2
import numpy as np

from collections import deque
import argparse
import imutils


cap = cv2.VideoCapture(0)
while (cap.isOpened()==False):     # This routine checks if the camera is opened yet or not 
        cap= cv2.VideoCapture(0)   # We don't want to run next part until the camera is open 


while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    lower_blue = np.array([29,86,6])      # for lower green 
    upper_blue = np.array([64,255,255])   #  for upper green 
    
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.erode(mask, None, iterations=2)          # reduces the noise around mask 
    mask = cv2.dilate(mask, None, iterations=2)         # fix the boundaries 
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
        
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
