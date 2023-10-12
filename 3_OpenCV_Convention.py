import cv2
import numpy as np

img = cv2.imread("Resouces/car.jpg")
print(img.shape)

imgResize = cv2.resize(img,(500,250))
print(imgResize.shape)

imgCropped = img[0:200,200:599]

cv2.imshow("Car Image",img)
#cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)