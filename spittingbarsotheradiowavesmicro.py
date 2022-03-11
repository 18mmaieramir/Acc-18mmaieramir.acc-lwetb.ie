import serial
import time


serialPort= serial.Serial(port = "COM3", baudrate=115200,
                          bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


serialString="cheese\n"

while(1):
    serialPort.write(serialString.encode())
    print('sent')
