import os
import sys
cwd=os.getcwd()            # Gets the current working directory of the file
(setpath,Examples)=os.path.split(cwd)  # Creates a tuple (head,tail) where tail is everything after the final slash
print setpath
sys.path.append(setpath)    #Appends the setpath to sys.path so as to provide a search path for the module Arduino

from Arduino.Arduino import Arduino       # Imports all the functions from module Arduino
from time import sleep

class SENSE:
    def __init__(self,baudrate):
        self.baudrate=baudrate
        self.setup()
        self.run()
        self.exit()
    def setup(self):
        self.obj_arduino=Arduino()
        self.port=self.obj_arduino.locateport()      #Locates the port 
        self.obj_arduino.open_serial(1,self.port,self.baudrate)
    def run(self):
        jlast=0
        k=0
        j=0
        self.pin1=9
        self.pin2=10
        self.intrp=5
        ilast=self.obj_arduino.cmd_digital_in(1,self.intrp)
        self.obj_arduino.cmd_dcmotor_setup(1,3,1,self.pin1,self.pin2)  # Initialize motor of the interrupt
        for s in range(5000):
            self.obj_arduino.cmd_dcmotor_run(1,1,100)    # Rotate the motor
            i=self.obj_arduino.cmd_digital_in(1,self.intrp)  # Read the signal of the receiver of IR sensor
            if i!=ilast:  # Check whether the motor is rotating
                if i=='1':  # Condition when the receiver receives the signal from transmitter
                    j=j+1
                sleep(0.01)
            ilast=i
            if j!=jlast:  
                print j
                if j%17==0 and j!=0:  # Condition for one complete rotation
                    k=k+1   # No of rotations
                    print 'number of rotations completed are',k
            jlast=j
        self.obj_arduino.cmd_dcmotor_release(1,1)

    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_sense=SENSE(115200)

if __name__=='__main__':   # To execute module as a script
    main()
