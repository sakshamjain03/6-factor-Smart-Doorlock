import RPi.GPIO as GPIO
import random
import time
import os
import serial
from time import sleep

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

from email.mime.text import MIMEText

from email import encoders

fromaddr = "vips0907@gmail.com"    # change the email address accordingly

msg = MIMEMultipart()

def sendMail():
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
    
def sendMail1(x):
    fromaddr = "vips0907@gmail.com"    # change the email address accordingly
    toaddr = "vips0907@gmail.com"
 
    msg = MIMEMultipart()
 
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Intruder Alert"
    text = "There is some activity in your office. See the attached picture."
    """msg.attach(MIMEText(text))
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
        'attachment; filename="%s"' % os.path.basename(x))
    msg.attach(part)"""
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
                                solenoid()
                            else:
                                print("PASSWORD INCORRECT")
                            
                        while(not GPIO.input(Row[i])):
                            pass
                GPIO.output(Col[j],1)
                


    except KeyboardInterrupt:
        GPIO.cleanup()

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
          
try:     
   while 1:
         #x=data.readline()#print the whole data at once
         #x=data.read()#print single data at once
         
         print ("Place the card")
         x=data.read(12)
         x=x.decode('UTF-8')#print upto 10 data at once and the 
                        #remaining on the second line
         
         if x=="40002830055D":
             print ("Card No - ",x)
             print ("Welcome Atharva")
             print (" ")
             toaddr = "wasraz86@gmail.com"
             sendMail()
         
         elif x=="400028341945":
             print ("Card No - ",x)
             print ("Welcome Simran")
             print (" ")
             toaddr = "simrunnpatil@gmail.com"
             sendMail()

         elif x=="400028422C06":
             print ("Card No - ",x)
             print ("Welcome Aditi")
             print (" ")
             toaddr = "aditiuk24@gmail.com"
             sendMail()

         else:
             print ("Wrong Card.....")
             print (" ")
             toaddr = "vips0907@gmail.com"#To the owner
             sendMail1(x)        
         
         #print x

except KeyboardInterrupt:
       data.close()