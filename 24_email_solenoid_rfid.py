import RPi.GPIO as GPIO
import random
import time
import os
import serial
from time import sleep
def sendMail(attach):
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
def solenoid():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
   
    GPIO.output(18, 0)
    sleep(10)
    GPIO.output(18, 1)
    exit

data = serial.Serial(
                    port='/dev/ttyUSB0',
                    baudrate = 9600,
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
         x = x.decode('UTF-8')#print upto 10 data at once and the 
                        #remaining on the second line

         if x=="40002830055D":
             print ("Card No - ",x)
             print ("Welcome Atharva")
             print (" ")
             toaddr = "atharvagpardeshi@gmail.com"
             sendMail()
         
         elif x=="400028341945":
             print ("Card No - ",x)
             print ("Welcome Simran")
             print (" ")
             toaddr = "simrunnpatil@gmail.com"
             sendMail()

         elif x=="400028473619":
             print ("Card No - ",x)
             print ("Welcome Wasif")
             print (" ")
             toaddr = "wasraz86@gmail.com"
             sendMail()

         else:
             print ("Wrong Card.....")
             print (" ")
             toaddr = "vips0907@gmail.com"#To the owner
             sendMail(x)        
         
         #print x

except KeyboardInterrupt:
       data.close()