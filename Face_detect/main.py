import cv2

face_cascade= cv2.CascadeClassifier('face.xml')

eye_casecade = cv2.CascadeClassifier('haarcascade_eye.xml')

for index in range(10):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Using index {index} for external webcam")
        break
    else:
        cap.release()
#result, img = cap.read()

while 1:
    ret, imag = cap.read()
    gray= cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)

    faces= face_cascade.detectMultiScale(gray, 1.1,5)

    for(x,y,height,width) in faces:
        cv2.rectangle(imag,(x,y),
                      (x+height,y+width),
                      (255,255,0),5)
        roi_gray= gray[y:y+height, x:x+width]
        roi_color = img[y:y+height, x:x+width]
        eye = eye_casecade.detectMultiScale(roi_gray)
        for(ex,ey,eheight,ewidth) in eye:
            cv2.rectangle(roi_color,(ex,ey),
                          (ex+eheight,ey+ewidth),
                          (255,255,0),2)
cv2.imshow('img',imag)
