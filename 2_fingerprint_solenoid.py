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
    
name=""

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
        global name
        if(positionNumber == 1):
            name = "Wasif"
        accuracyScore = result[1]
        if positionNumber == -1 :
            print('No match found!')
            global cnt
            cnt += 1
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            solenoid()
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
    
fl=1
cnt = 0
#searchFinger()
#enrollFinger()
#solenoid()
fl=1
cnt=0
def fingerPrint():
    global fl
    global cnt
    global name

    while fl:
        gpio.output(led, HIGH)
        searchFinger()
        print(cnt)
        if(cnt==3):
            break

    cnt=0
    fl=1
    print(name)
        
fingerPrint()

# while fl:
#     gpio.output(led, HIGH)
#     searchFinger()
#     if(cnt==3):
#         break
