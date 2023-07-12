import time
import serial
import os
          
      
data = serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',baudrate = 115200,timeout=1.0,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
                    #timeout=1 # must use when using data.readline()
                    #)
print(" ")

print("Place the card")
x=data.read(12)#print upto 10 data at once and the 
                        #remaining on the second line
print(x)