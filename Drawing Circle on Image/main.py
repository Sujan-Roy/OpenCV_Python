import cv2
import matplotlib.pyplot as plt
# Read the input image
image = cv2.imread("dataset/flower.jpg")

plt.subplot(2,2,1)
plt.title("Orginal Image")
plt.imshow(image)
#cv2.imshow("Orginal Image",image)

circle = cv2.circle(image,(80,80),50, (255,255,0),-1)
#cv2.imshow("Circle image", circle)
plt.subplot(2,2,2)
plt.title("Circle Image")
plt.imshow(circle)

# titles = ["Orginal Image","circle Image"]
# images= [image,circle]
# count = 2

# def imageshow(title,):
#     plt.subplot(2,2,1)
#     plt.title(titles[i])
#     plt.imshow(images[i])
plt.show()
#cv2.waitKey()
