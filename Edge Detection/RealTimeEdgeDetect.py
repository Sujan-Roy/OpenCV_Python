import cv2

cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
if not (cap.isOpened()):
    print("Please check the cmarea from device manger in windows")
while True: 
    ret,frame = cap.read()
    #cap.ret(cv2.CAP_PROP_FRAME_WIDTH , 720) #// you should chose a value that the camera supports
    #cap.ret(cv2.CAP_PROP_FRAME_HEIGHT ,720) #// you should chose a value that the camera supports
    cv2.imshow("Live",frame)
    edges= cv2.Canny(frame,100,100)
    cv2.imshow("Edge",edges)
    cap.release()
    cv2.waitKey(0)
cv2.destroyAllWindows()


# cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# if not (cap.isOpened()):
#     print("Could not open video device")
# while True: 
#     ret,frame= cap.read()
#     cv2.imshow("Live",frame)
#     cv2.waitKey(1)
# cv2.destroyAllWindows()