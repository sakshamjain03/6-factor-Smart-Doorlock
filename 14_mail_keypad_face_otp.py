import face_recognition
import RPi.GPIO as GPIO
import random
import time

import numpy as np

import cv2

from datetime import datetime

import os

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

from email.mime.text import MIMEText

from email import encoders

fromaddr = "vips0907@gmail.com"    # change the email address accordingly

msg = MIMEMultipart()

def sendMail():
    os.remove(picname)
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Attachment"
    number = random.randint(1000,9999)    
    text = "Your OTP is "+str(number)#,". Please enter your OTP" 
    msg.attach(MIMEText(text))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "viaps@1618")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Email Sent")
    Keypad(number)
    server.quit()
    
def sendMail1(attach):
    fromaddr = "vips0907@gmail.com"    # change the email address accordingly
    toaddr = "vips0907@gmail.com"
 
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
    mailServer.login(fromaddr, "viaps@1618")
    mailServer.sendmail(fromaddr, toaddr, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    print("Email Sent")
    mailServer.close()

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
                                print("ACCESS GRANTED")
                            else:
                                print("PASSWORD INCORRECT")
                            
                        while(not GPIO.input(Row[i])):
                            pass
                GPIO.output(Col[j],1)
                


    except KeyboardInterrupt:
        GPIO.cleanup()

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

cap = cv2.VideoCapture(0)

print ("Saving Photo")

picname = datetime.now().strftime("%y-%m-%d-%H-%M")

picname = picname+'.jpg'
cv2.imwrite(picname, frame)
attach = picname

picture1_of_me = face_recognition.load_image_file("Atharva.jpg")
my_face1_encoding = face_recognition.face_encodings(picture1_of_me)[0]

picture2_of_me = face_recognition.load_image_file("Salman.jpg")
my_face2_encoding = face_recognition.face_encodings(picture2_of_me)[0]

picture3_of_me = face_recognition.load_image_file("Bieber.jpg")
my_face3_encoding = face_recognition.face_encodings(picture3_of_me)[0]

picture4_of_me = face_recognition.load_image_file("Shahrukh.jpg")
my_face4_encoding = face_recognition.face_encodings(picture4_of_me)[0]



unknown_picture = face_recognition.load_image_file(picname)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

if face_recognition.compare_faces([my_face2_encoding], unknown_face_encoding)[0] == True:
     print("This is salman")
        
elif face_recognition.compare_faces([my_face3_encoding], unknown_face_encoding)[0] == True:
     print("This is bieber")

elif face_recognition.compare_faces([my_face4_encoding], unknown_face_encoding)[0] == True:
     print("This is Shahrukh")
     
     
elif face_recognition.compare_faces([my_face1_encoding], unknown_face_encoding)[0] == True:
     print("This is Atharva")
     toaddr = "atharvagpardeshi@gmail.com"
     sendMail()
        
else:
     print("Unknown picture")
     toaddr = "vips0907@gmail.com"#To the owner
     sendMail1(attach)