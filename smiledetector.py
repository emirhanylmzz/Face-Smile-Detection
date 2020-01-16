# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:29:12 2019
Emirhan YILMAZ CV & AI HOMEWORK (SMİLE DETECTOR)
@author: emirhanylmzz
"""
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 22)
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (ax, ay, aw, ah) in smiles:
            cv2.rectangle(roi_color, (ax, ay), (ax+aw, ay+ah), (0, 0, 255), 2)
    return frame

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    #frame = cv2.resize(frame, None, fx=1, fy=1 , interpolation=cv2.INTER_AREA)
    if ret:    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = detect(gray, frame)
        cv2.imshow('Video', canvas) #Display the outputs.
        if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard:
            break # Stop the loop.
    else:
        print("Couldn't")
video_capture.release() # Turning the webcam off.
cv2.destroyAllWindows() 
