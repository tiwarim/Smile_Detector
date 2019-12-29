#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:12:11 2019

@author: mrinal
"""

# import libraries
import cv2

# make cascade objects
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')



# define a fuction to detect face, eyes and the smile

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # downscale to 1.3 with 5 neighbours
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w ]
        roi_frame = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22) #downscale to 1.1 with 22 neighbours
                                          # we use 22 neighbours to increase precision
        
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        
        for(sx, sy, sw, sh) in  smiles:
            cv2.rectangle(roi_frame, (sx, sy), (sx+sw, sy+sh), (0,0, 255), 2)
            
    return frame


video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # color to grayscale
    detected = detect(gray, frame) # detect face, eyes and smile
    
    cv2.imshow('video', detected) # make a video with the detected image returned

    if cv2.waitKey(1) & 0xFF == ord('q'): # quit when q is pressed
        break
    
video.release()
cv2.destroyAllWindows()
            