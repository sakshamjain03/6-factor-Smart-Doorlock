import serial     #import serial module

def read_rfid ():
   ser = serial.Serial ("/dev/ttyUSB0")#Open named port 
   ser.baudrate = 9600         #Set baud rate to 9600
   data = ser.read(12)         #Read 12 characters from serial port to data
   ser.close ()                #Close port
   return data                 #Return data

id = read_rfid ()              #Function call
print(id)                      #Print RFID