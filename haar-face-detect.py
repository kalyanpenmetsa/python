####Download numpy and opencv-python modules using pip install
import numpy as np
import cv2
####Image Input and Haar filter xml input (FULL PATH)
####Download haarcascade filters from https://github.com/opencv/opencv/tree/master/data/haarcascades ####
img ='media/group.jpg'
haar_filter = 'data/haarcascades/haarcascade_frontalface_alt.xml'

####Function to show Image ### show_image(img,timeInterval)
def show_image(image,timeInterval=2000):
    img = cv2.imread(image)
    cv2.imshow('show_image', img)
    cv2.waitKey(timeInterval)
    cv2.destroyAllWindows()

####Function for Face Detection ### face_detect(haar_filter,image,scalefactor,minNeighbor,timeInterval)
def face_detect(haar_filter,image,scalefactor=1.1,minNeighbor=5,timeInterval=2000):
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    haar_face_cascade = cv2.CascadeClassifier(haar_filter)
    faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=scalefactor, minNeighbors=minNeighbor)
    print('Faces found: ', len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('show_image', img)
    cv2.waitKey(timeInterval)
    cv2.destroyAllWindows()

#### show_image and face_detect run
show_image(img)
face_detect(haar_filter,img)
