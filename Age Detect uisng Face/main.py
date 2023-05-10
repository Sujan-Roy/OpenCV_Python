import cv2
import numpy as np

# Load the face detector model.
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the age detector model.
age_detector = cv2.dnn.readNet('age_net.caffemodel', 'age_deploy.prototxt')

