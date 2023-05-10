import cv2
import numpy as np

# Load the face detector model.
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the age detector model.
age_detector = cv2.dnn.readNet('age_net.caffemodel', 'age_deploy.prototxt')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, imag = cap.read()
    gray= cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)

    cv2.imshow('img',imag)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()