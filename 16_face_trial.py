import RPi.GPIO as GPIO
import random
import time
import os
import serial 
from time import sleep

import deepface
from deepface import DeepFace
import os
#!/bin/bash fswebcam -r 1280*960 /home/pi/Desktop/saved_pic/$test.jpg
import cv2

cam = cv2.VideoCapture(0)


ret, image = cam.read()
cv2.imshow('Imagetest',image)
	
name=""
cv2.imwrite('/home/pi/Desktop/saved_pic/test.jpg', image)
cam.release()
cv2.destroyAllWindows()
metrics = ["cosine", "euclidean","euclidean_l2"]
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
#path of database to be put in db_path
#path of testing images to be put in img_path
#face recognition
try:
    df = DeepFace.find(img_path = "/home/pi/Desktop/saved_pic/test.jpg", db_path = "/home/pi/Desktop/caps_img", model_name = models[7], distance_metric = metrics[1])
#path of representations_vgg_face.pkl to be put here
    os.remove("/home/pi/Desktop/caps_img/representations_dlib.pkl")
    os.remove("/home/pi/Desktop/saved_pic/test.jpg")
#print(df.head(1))

    if(df['Dlib_euclidean'][0]<0.5):
        print(df['identity'][0])
    
    else:
        name="Unknown picture"
        print("Unknown picture")

except:
    name="No face detected"
    print("No face detected")
if name!="No face detected" and name!="Unknown picture":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
   
    GPIO.output(18, 0)
    sleep(10)
    GPIO.output(18, 1)
    exit