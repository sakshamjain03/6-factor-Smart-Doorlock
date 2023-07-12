import RPi.GPIO as GPIO
import random
import time

number = random.randint(1000,9999)
print(number)
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