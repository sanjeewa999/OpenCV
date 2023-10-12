import cv2
import numpy as np

kernal = np.ones((5,5),np.uint8)

img = cv2.imread("Resouces/img.jpg")

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(grayImg,(7,7),0)  # ksize should be odd numbers ex:(5,5) (3,3) (7,7)
cannyImg = cv2.Canny(blurImg,100,100)  # View the edges of image
dialationImg = cv2.dilate(cannyImg,kernal,iterations=1)
erodedImg = cv2.erode(dialationImg,kernal,iterations=1)

# cv2.imshow("Gray Image",grayImg)
# cv2.imshow("Blur Image",blurImg)
cv2.imshow("Canny Image",cannyImg)
cv2.imshow("Dialation Image",dialationImg)
cv2.imshow("Eroded Image",erodedImg)
cv2.waitKey(0)