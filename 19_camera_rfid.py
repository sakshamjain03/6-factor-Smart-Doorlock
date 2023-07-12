import time
start1 = time.process_time()
import RPi.GPIO as GPIO
import random

import os
import serial
from time import sleep
import deepface
from deepface import DeepFace
#!/bin/bash fswebcam -r 1280*960 /home/pi/Desktop/saved_pic/$test.jpg
import cv2
import time
start = time.process_time()
# your code here    

def solenoid():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
   
    GPIO.output(17, 0)
    sleep(10)
    GPIO.output(17, 1)
    exit

data = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
                    #timeout=1 # must use when using data.readline()
                    #)
print (" ")

name=""
print ("Place the card")
x=data.read(12)#print upto 10 data at once and the 
                        #remaining on the second line
x = x.decode('UTF-8')
if x=="400028422C06":
    print ("Card No - ",x)
    print ("Welcome Atharva")
    name="Atharva"
    print (" ")
             #toaddr = "atharvagpardeshi@gmail.com"
             #sendMail()
         
elif x=="4000288DB055":#"400028341945":
    print ("Card No - ",x)
    print ("Welcome Simran")
    name="Simran"
    print (" ")
             #toaddr = "simrunnpatil@gmail.com"
             #sendMail()
             
elif x=="400028473619":
    print ("Card No - ",x)
    print ("Welcome Wasif")
    name="Wasif"
    print (" ")
elif x=="400031AECB14":
    print ("Card No - ",x)
    print ("Welcome Trushita")
    name="Trushita"
    print (" ")
elif x=="400028550E33":#"400028341945":
    print ("Card No - ",x)
    print ("Welcome Shweta")
    name="Shweta"
    print (" ")
elif x=="4000282EEBAD":#"400028341945":
    print ("Card No - ",x)
    print ("Welcome Shreekant")
    name="Shreekant"
    print (" ")
else:
    print ("Card No - ",x)
    print ("Wrong Card.....")
    name="Wrong"
    print (" ")            
         #print x
#print("Rfid time",time.process_time() - start1)


data.close()
if(name!="Wrong"):
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    cv2.imshow('Imagetest',image)
	
    cv2.imwrite('/home/pi/Desktop/saved_pic/test.jpg', image)
    cam.release()
    cv2.destroyAllWindows()
    metrics = ["cosine", "euclidean","euclidean_l2"]
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
    #path of database to be put in db_path
    #path of testing images to be put in img_path
    #face recognition
    try:
        if(name=="Trushita"):
            df = DeepFace.find(img_path = "/home/pi/Desktop/saved_pic/test.jpg", db_path = "/home/pi/Desktop/Trushita_Chaware", model_name = models[7], distance_metric = metrics[1])
            os.remove("/home/pi/Desktop/Trushita_Chaware/representations_dlib.pkl")

        elif(name=="Atharva"):
            df = DeepFace.find(img_path = "/home/pi/Desktop/saved_pic/test.jpg", db_path = "/home/pi/Desktop/Atharva", model_name = models[7], distance_metric = metrics[1])
            os.remove("/home/pi/Desktop/Atharva/representations_dlib.pkl")
    #path of representations_vgg_face.pkl to be put here
        elif(name=="Wasif"):
            
            df = DeepFace.find(img_path = "/home/pi/Desktop/saved_pic/test.jpg", db_path = "/home/pi/Desktop/Wasif", model_name = models[7], distance_metric = metrics[1])
            os.remove("/home/pi/Desktop/Wasif/representations_dlib.pkl")
        elif(name=="Shweta"):
            df = DeepFace.find(img_path = "/home/pi/Desktop/saved_pic/test.jpg", db_path = "/home/pi/Desktop/Shweta_Kukade", model_name = models[7], distance_metric = metrics[1])
            os.remove("/home/pi/Desktop/Shweta_Kukade/representations_dlib.pkl")

        elif(name=="Shreekant"):
            
            df = DeepFace.find(img_path = "/home/pi/Desktop/saved_pic/test.jpg", db_path = "/home/pi/Desktop/Shreekant", model_name = models[7], distance_metric = metrics[1])
            os.remove("/home/pi/Desktop/Shreekant/representations_dlib.pkl")
        elif(name=="Simran"):
            
            df = DeepFace.find(img_path = "/home/pi/Desktop/saved_pic/test.jpg", db_path = "/home/pi/Desktop/Simran", model_name = models[7], distance_metric = metrics[1])
            os.remove("/home/pi/Desktop/Simran/representations_dlib.pkl")


        
        os.remove("/home/pi/Desktop/saved_pic/test.jpg")
        #print(df.head(1))

        if(df['Dlib_euclidean'][0]<0.5):
            print(df['identity'][0])
            print(name," face detected")
            solenoid()
    
        else:
            print("Unknown picture")

    except:
        print("No face detected")
#print("Total time",time.process_time() - start)