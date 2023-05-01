import cv2
import matplotlib.pyplot as plt

image = cv2.imread("dataset/dog.jpg")

## average Blur

blurImage= cv2.blur(image,(3,3))
MedianImage = cv2.GaussianBlur(image,(5,5),cv2.BORDER_TRANSPARENT)

plt.subplot(2,2,1)
plt.title("Orginal Image")
plt.imshow(image)

plt.subplot(2,2,2)
plt.title("Blur on Image")
plt.imshow(blurImage)

plt.subplot(2,2,3)
plt.title("Median Image")
plt.imshow(MedianImage)
plt.show()