f = open("light.txt" ,"a+")


def light():

    import serial



    serialPort = serial.Serial(port = "COM3", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


    serialString=""




    while(1):
        if(serialPort.in_waiting > 0):
            serialString= serialPort.readline()
            f.write(serialString.decode("Ascii"))
            
            
