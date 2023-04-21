import cv2
import matplotlib.pyplot as plt
## Read an image from dataset
img = cv2.imread("dataset/flower.jpg")

### Down scaling
scale =50

width =int (img.shape[1]*scale/100)
height = int(img.shape[0]*scale/100)

reshape= (width,height)
resize_image = cv2.resize(img,reshape,interpolation=cv2.INTER_AREA)

plt.subplot(2,2,1), plt.imshow(img),plt.title("Orginal image")
plt.subplot(2,2,2), plt.imshow(resize_image),plt.title("Resize image")
plt.show()
# cv2.imshow('original',resize_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


## Up scaling

scale1= 150

# Resize the specified width and height
width1 = 350  
height1 = 450  
