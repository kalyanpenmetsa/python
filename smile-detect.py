####Download numpy and opencv-python modules using pip install
import cv2
import numpy as np
import sys

####Download face and smile filters from https://github.com/opencv/opencv/tree/master/data/haarcascades/ ####
faceFilter = 'data/haarcascades/haarcascade_frontalface_default.xml'
smileFilter = 'data/haarcascades/haarcascade_smile.xml'

faceCascade = cv2.CascadeClassifier(faceFilter)
smileCascade = cv2.CascadeClassifier(smileFilter)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, frame = cap.read()
#    vid = cv2.cvtColor(frame, 0)
    vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(vid, scaleFactor=1.05, minNeighbors=8, minSize=(55, 55))
    cv2.imshow('frame', vid)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        smile = smileCascade.detectMultiScale(vid, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
        # print("Found", len(smile), "smiles!")
        for (x, y, w, h) in smile:
            print("Found", len(smile), "smiles!")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
