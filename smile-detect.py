import cv2
import numpy as np
# import sys
faceFilter =  'data/haarcascades/haarcascade_frontalface_default.xml'
smileFilter = 'data/haarcascades/haarcascade_smile.xml'
eyeFilter = 'data/haarcascades/haarcascade_eye.xml'

def scanCamera(faceCascade,smileCascade,eyeCascade):
    faceCascade = cv2.CascadeClassifier(faceFilter)
    smileCascade = cv2.CascadeClassifier(smileFilter)
    eyeCascade = cv2.CascadeClassifier(eyeFilter)

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # set Width
    cap.set(4, 480)  # set Height

    while True:
        ret, frame = cap.read()
        # vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vid = cv2.cvtColor(frame, 0)
        faces = faceCascade.detectMultiScale(vid, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

        for (x, y, w, h) in faces:
            cv2.rectangle(vid, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = vid[y:y + h, x:x + w]
            roi_color = vid[y:y + h, x:x + w]

            smile = smileCascade.detectMultiScale(frame, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
            for (x, y, w, h) in smile:
                print("Found", len(smile), "smiles!")
                cv2.rectangle(vid, (x, y), (x + w, y + h), (255, 0, 0), 2)
            eye = eyeCascade.detectMultiScale(frame, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
            for (x, y, w, h) in eye:
                print("Found", len(eye), "eyes!")
                cv2.rectangle(vid, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('frame', vid)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

scanCamera(faceFilter,smileFilter,eyeFilter)
