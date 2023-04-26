import cv2
image= cv2.imread("dataset/cat.jpg")
Text = cv2.putText(image,"Orginal Image",(40,40),cv2.FONT_ITALIC,1,(255,255,0),1)
edgedetect= cv2.Canny(image,80,120)

cv2.imshow("Original Image",Text)
cv2.imshow("Edge", edgedetect)

cv2.waitKey(0)
cv2.destroyAllWindows()

