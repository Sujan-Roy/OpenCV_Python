import cv2
import matplotlib.pyplot as plt
# Read the input image
image = cv2.imread("dataset/flower.jpg")
image2 = cv2.imread("dataset/cat.jpg")
image3 = cv2.imread("dataset/dog.jpg")

plt.subplot(2,3,1)
plt.title("Orginal Image")
plt.imshow(image)
#cv2.imshow("Orginal Image",image)

# Circle on Image
circle1 = cv2.circle(image,(480,580),180, (255,255,0),1) 
# 1 denotes the thickness of the circle outline, if it is positive. 

#cv2.imshow("Circle image", circle)
plt.subplot(2,3,2)
plt.title("Circle Image1")
plt.imshow(circle1)

circle2 = cv2.circle(image,(580,580),280, (255,0,250),-1)
# -1denotes the thickness of the circle outlinethat a filled circle is to be drawn.
plt.subplot(2,3,3)
plt.title("Circle Image2")
plt.imshow(circle2)

# Rectange on Image

rectange= cv2.rectangle(image2,(350,200),(10,10),(0,255,0),5)
plt.subplot(2,3,4)
plt.title("Rectange Image")
plt.imshow(rectange)

Elipsis = cv2.ellipse(image3,(150,170),(90,30),15,0,360,(255,135,0),-1)
Text= cv2.putText(Elipsis,'Ellipise Image',(20,60),cv2.FONT_HERSHEY_PLAIN,3,(255,120,255),3)
plt.subplot(2,3,5)
plt.title("Ellipse Image")
plt.imshow(Text)



# titles = ["Orginal Image","circle Image"]
# images= [image,circle]
# count = 2

# def imageshow(title,):
#     plt.subplot(2,2,1)
#     plt.title(titles[i])
#     plt.imshow(images[i])
plt.show()
#cv2.waitKey()
