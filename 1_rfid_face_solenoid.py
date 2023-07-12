import deepface
from deepface import DeepFace
import os
import cv2
import serial  
import time
import RPi.GPIO as GPIO
from time import sleep
data = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
def solenoid():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
   
    GPIO.output(17, 0)
    sleep(5)
    GPIO.output(17, 1)
    sleep(5)
    data.close()
    #tput reset > /dev/ttyXX
    exit
    
def rfid():
    
                    #timeout=1 # must use when using data.readline()
                    #)
    print(" ")

          

         #x=data.readline()#print the whole data at once
         #x=data.read()#print single data at once
         
    print("Place the card")
    x=data.read(12)
    x=x.decode('UTF-8')#print upto 10 data at once and the 
                        #remaining on the second line
         
    if x=="400028473619":
        print("Card No - ",x)
        print("Welcome Simran")
        print(" ")
        solenoid()
         
    elif x=="4000288DB055" and (name[len(name)-12:]=="atharva1.jpg" or name[len(name)-12:]=="atharva2.jpg" or name[len(name)-12:]=="atharva3.jpg" or name[len(name)-12:]=="atharva4.jpg"):
        print("Card No - ",x)
        print("Welcome Atharva")
        print(" ")
        solenoid()
             
    elif x=="400028341945":
        print("Card No - ",x)
        print("Welcome Aditi")
        print(" ")
        solenoid()
             
             
         #elif x=="400028422C06":
             #print("Card No - ",x)
             #print("Welcome Samrudhi")
             #print(" ")
             
             
    elif x=="40002830055D" and (name[len(name)-10:]=="wasif1.jpg" or name[len(name)-10:]=="wasif2.jpg" ):
        print("Card No - ",x)
        print("Welcome Wasif")
        print(" ")
    else:
        print("Wrong Card.....")
        print(" ")        
         
    print(x)

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
    #print(df.head(1))

    if(df['Dlib_euclidean'][0]<0.5):
        name=df['identity'][0]
        print(df['identity'][0])
        
    
    else:
        name="Unknown picture"
        print("Unknown picture")

except:
    name="No face detected"
    print("No face detected")

rfid()
os.remove("/home/pi/Desktop/saved_pic/test.jpg")
