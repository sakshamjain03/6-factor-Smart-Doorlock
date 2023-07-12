#!/bin/bash fswebcam -r 1280*960 /home/pi/Desktop/saved_pic/$test.jpg
import cv2

cam = cv2.VideoCapture(0)


ret, image = cam.read()
cv2.imshow('Imagetest',image)
	
cv2.imwrite('/home/pi/Desktop/saved_pic/test.jpg', image)
cam.release()
cv2.destroyAllWindows()