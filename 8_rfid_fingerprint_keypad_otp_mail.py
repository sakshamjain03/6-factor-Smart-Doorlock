import serial
import time
from time import sleep
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio


RS =18
EN =23
D4 =24
D5 =25
D6 =8
D7 =7
enrol=5
delet=6
inc=13
dec=19
led=26


HIGH=1

LOW=0


gpio.setwarnings(False)

gpio.setmode(gpio.BCM)

gpio.setup(RS, gpio.OUT)

gpio.setup(EN, gpio.OUT)

gpio.setup(D4, gpio.OUT)

gpio.setup(D5, gpio.OUT)

gpio.setup(D6, gpio.OUT)

gpio.setup(D7, gpio.OUT)

gpio.setup(enrol, gpio.IN, pull_up_down=gpio.PUD_UP)

gpio.setup(delet, gpio.IN, pull_up_down=gpio.PUD_UP)

gpio.setup(inc, gpio.IN, pull_up_down=gpio.PUD_UP)

gpio.setup(dec, gpio.IN, pull_up_down=gpio.PUD_UP)

gpio.setup(led, gpio.OUT)

try:

    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)


    if ( f.verifyPassword() == False ):

        raise ValueError('The given fingerprint sensor password is wrong!')


except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)

def enrollFinger():
    print("Enrolling Finger")
    time.sleep(2)
    print('Waiting for finger...')
    print("Place Finger")
    while ( f.readImage() == False ):
        pass
    f.convertImage(0x01)
    result = f.searchTemplate()
    positionNumber = result[0]
    if ( positionNumber >= 0 ):
        print('Template already exists at position #' + str(positionNumber))
        time.sleep(2)
        return
    print('Remove finger...')
    time.sleep(2)
    print('Waiting for same finger again...')
    while ( f.readImage() == False ):
        pass
    f.convertImage(0x02)
    if ( f.compareCharacteristics() == 0 ):
        print("Fingers do not match")
        time.sleep(2)
        return
    f.createTemplate()
    positionNumber = f.storeTemplate()
    print('Finger enrolled successfully!')
    print('New template position #' + str(positionNumber))
    time.sleep(2)


fl=1
cnt=0
nme=""
name=""
def fingerPrint():
    global fl
    global cnt
    global nme
    while fl:
        gpio.output(led, HIGH)
        searchFinger()
        if(cnt==3):
            break
    cnt=0
    fl=1
    
def searchFinger():
    try:
        print('Waiting for finger...')
        while( f.readImage() == False ):
            #pass
            time.sleep(.5)
            return
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        global nme
        print("position number ", positionNumber)
        if(positionNumber == 1 or positionNumber == 0):
            nme = "Wasif"
        accuracyScore = result[1]
        if positionNumber == -1 :
            print('No match found!')
            global cnt
            cnt += 1
            time.sleep(2)
            return
        
        else:            
            if(nme==name):
                print("Welcome " + nme)
                solenoid()
            else:
                print("Fingerprint Mismatch")
                
            global fl
            fl=0
            time.sleep(2)
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)    

def deleteFinger():
    positionNumber = 0
    count=0
    while gpio.input(enrol) == True:   # here enrol key means ok
        if gpio.input(inc) == False:
            count=count+1
            if count>1000:
                count=1000
            time.sleep(0.2)
        elif gpio.input(dec) == False:
            count=count-1
            if count<0:
                count=0
            time.sleep(0.2)
    positionNumber=count
    if f.deleteTemplate(positionNumber) == True :
        print('Template deleted!')
        time.sleep(2)
def solenoid():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)   
    gpio.output(17, 0)
    sleep(10)
    gpio.output(17, 1)
    exit
    

      
data = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
print (" ")


print ("Place the card")
x=data.read(12)#print upto 10 data at once and the 
                        #remaining on the second line
x = x.decode('UTF-8')
if x=="400028422C06":
    print ("Card No - ",x)
    print ("Welcome Atharva")
    name="Atharva"
    print (" ")
    fingerPrint()
             #toaddr = "atharvagpardeshi@gmail.com"
             #sendMail()
         
elif x=="4000288DB055":#"400028341945":
    print ("Card No - ",x)
    print ("Welcome Simran")
    name="Simran"
    print (" ")
    fingerPrint()
             #toaddr = "simrunnpatil@gmail.com"
             #sendMail()
             
elif x=="400028473619":
    print ("Card No - ",x)
    print ("Welcome Wasif")
    name="Wasif"
    print (" ")
    fingerPrint()
    
elif x=="400031AECB14":
    print ("Card No - ",x)
    print ("Welcome Trushita")
    name="Trushita"
    print (" ")
    fingerPrint()
    
elif x=="400028550E33":#"400028341945":
    print ("Card No - ",x)
    print ("Welcome Shweta")
    name="Shweta"
    print (" ")
    fingerPrint()
    
elif x=="40002840C3EB":#"400028341945":
    print ("Card No - ",x)
    print ("Welcome Aditi")
    name="Aditi"
    print (" ")
    fingerPrint()
    
else:
    print ("Card No - ",x)
    print ("Wrong Card.....")
    name="Wrong"
    print (" ")            


data.close()
