import cv2
########## IMPORT IMAGE ##########

# img = cv2.imread("Resouces/img.jpg")
# cv2.imshow("image",img)
# cv2.waitKey(0)

########## IMPORT VIDEO ##########

# vid = cv2.VideoCapture("Resouces/vid.mp4")
#
# while True:
#     status , frame = vid.read()   #Read frame by frame as images. Status is use to indicate whether read sucess or not. it returns a boolean value.
#     cv2.imshow("video",frame)
#     if(cv2.waitKey(1) & 0xFF ==ord('q')):
#         break

########## WEB CAM ##########

webcam = cv2.VideoCapture(0)
webcam.set(3,640)
webcam.set(4,480)
webcam.set(10,100)  #brighnes set to 100

while True:
    status , img = webcam.read()
    cv2.imshow("webcam feed",img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break