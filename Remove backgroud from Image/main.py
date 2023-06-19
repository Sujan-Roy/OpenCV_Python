import cv2
import os
from rembg import remove
import matplotlib.pyplot as plt

newPath="Output_Image_directory/"

#Create new directory if the diserd directory is not exist
if not os.path.exists(newPath):
    os.makedirs(newPath)


image = cv2.imread("dataset/flower.jpg")
output_image=remove(image)

output_path = os.path.join(newPath, "flower.jpg")
cv2.imwrite(output_path, output_image)

#output_image.save("newPath/dog.jpg")
plt.subplot(2,2,1)
plt.title("Orginal Image")
plt.imshow(image)
plt.subplot(2,2,2)
plt.title("Back Image")
plt.imshow(output_image)

plt.show()