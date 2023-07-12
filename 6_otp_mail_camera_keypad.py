import face_recognition
import RPi.GPIO as GPIO
import random
import time
from time import sleep
import numpy as np
import cv2
from datetime import datetime
import os
import smtplib
import serial 
from time import sleep
import deepface
from deepface import DeepFace

#changes:
#in send maill() - toaddr = "wasraz86@gmail.com" to ---


from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

from email.mime.text import MIMEText

from email import encoders

#fromaddr = "vips0907@gmail.com"    # change the email address accordingly
fromaddr = "doorlock.mitwpu@gmail.com"


#!/bin/bash fswebcam -r 1280*960 /home/pi/Desktop/saved_pic/$test.jpg
#old password = "viaps@1618"

msg = MIMEMultipart()

def sendMail():
    #os.remove(picname)
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Attachment"
    number = random.randint(1000,9999)    
    text = "Your OTP is "+str(number)#,". Please enter your OTP" 
    msg.attach(MIMEText(text))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "vhvxibussncacnks")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Email Sent")
    Keypad(number)
    server.quit()
    
def sendMail1(attach):
    #fromaddr = "vips0907@gmail.com"    # change the email address accordingly
    fromaddr = "doorlock.mitwpu@gmail.com"
    toaddr = "user's_mailID"
 
    msg = MIMEMultipart()
 
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Intruder Alert"
    text = "There is some activity in your office. See the attached picture."
    msg.attach(MIMEText(text))
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
        'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(fromaddr, "vhvxibussncacnks")
    mailServer.sendmail(fromaddr, toaddr, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    print("Email Sent")
    mailServer.close()

def solenoid():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
   
    GPIO.output(17, 0)
    sleep(5)
    GPIO.output(17, 1)
    exit

def Keypad(number):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    Matrix =[[1,2,3,'A'],
             [4,5,6,'B'],
             [7,8,9,'C'],
             ['*',0,'#','D']]
    b=[]
    f=0

    pwd = [int(x) for x in str(number)]
    Row = [18,23,24,25]
    Col = [5,6,13,26]

    for j in range(4):
        GPIO.setup(Col[j],GPIO.OUT)
        GPIO.output(Col[j],1)

    for i in range(4):
        GPIO.setup(Row[i],GPIO.IN,pull_up_down = GPIO.PUD_UP)
    print("Press * to enter passcode ")
    try:
        while True:
            time.sleep(0.2)
            for j in range(4):
                GPIO.output(Col[j],0)
                for i in range(4):
                    if (not GPIO.input(Row[i])):
                        print(Matrix[i][j])
                        a=Matrix[i][j]
                        
                        if a=='*':
                            print("Enter passcode")
                        if a!='*':
                            b.append(Matrix[i][j])
                        if a=='A':
                            for i in range(4):
                                if b[i]!=pwd[i]:
                                    f=1
                                    break
                            if f==0:
                                access="ACCESS GRANTED"
                                print("ACCESS GRANTED")
                                solenoid()
                            else:
                                print("PASSWORD INCORRECT")
                            
                        while(not GPIO.input(Row[i])):
                            pass
                GPIO.output(Col[j],1)
                


    except KeyboardInterrupt:
        GPIO.cleanup()

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

attach="/home/pi/Desktop/saved_pic/test.jpg"
if(name[len(name)-12:]=="atharva1.jpg" or name[len(name)-12:]=="atharva2.jpg" or name[len(name)-12:]=="atharva3.jpg" or name[len(name)-12:]=="atharva4.jpg"):
    print("This is Atharva")
    toaddr = "user's_mailID"
    sendMail()
        
elif(name[len(name)-10:]=="wasif1.jpg" or name[len(name)-10:]=="wasif2.jpg" ):
    print("This is Wasif")
    toaddr = "user's_mailID"
    sendMail()
        
else:
    print("Unknown picture")
    toaddr = "user's_mailID"#To the owner
    sendMail1(attach)
os.remove("/home/pi/Desktop/saved_pic/test.jpg")

