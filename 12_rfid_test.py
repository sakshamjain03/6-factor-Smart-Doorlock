import time
import serial
import RPi.GPIO as GPIO
from time import sleep

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
    
      
data = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
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
         
elif x=="4000288DB055":
    print("Card No - ",x)
    print("Welcome Simran")
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
             
             
         #elif x=="40002830055D":
             #print("Card No - ",x)
             #print("Welcome Wasif")
             #print(" ")
else:
    print("Wrong Card.....")
    print(" ")        
         
print(x)

