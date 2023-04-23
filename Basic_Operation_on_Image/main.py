# To find the image height, width and channel
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower.jpg")
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# To show the orginal Image
#cv2.imshow("Orginal Image",gray)

height= img.shape[0]
width= img.shape[1]
channel = img.shape[2]
img_size= img.size

print("Image Heightz: ",height)
print("Image Width: ",width)
print("Image channel: ",channel)
print("Image size: ",img_size)

height= gray.shape[0]
width= gray.shape[1]

img_size= gray.size


print("Image Heightz: ",height)
print("Image Width: ",width)

print("Image size: ",img_size)

# To show the BGG from an Image
b,g,r=cv2.split(img)
print("B=",b)
print("G= ",g)
print("R= ",r)

# Making Border of an Image

replicate= cv2.copyMakeBorder(img,40,40,20,20,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,20,20,cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img,10,10,20,20,cv2.BORDER_REFLECT_101)
wrap  = cv2.copyMakeBorder(img,10,10,20,20,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,40,40,40,40,cv2.BORDER_CONSTANT,value=(255,0,0))


plt.subplot(231), plt.imshow(replicate,'gray'), plt.title('Replicate')
plt.subplot(232), plt.imshow(reflect,'gray'), plt.title('reflect')
plt.subplot(233), plt.imshow(reflect_101,'gray'), plt.title('reflect_101')
plt.subplot(234), plt.imshow(wrap,'gray'), plt.title('wrap')
plt.subplot(235), plt.imshow(constant,'gray'), plt.title('constant')
plt.show()

cv2.waitKey(0)
