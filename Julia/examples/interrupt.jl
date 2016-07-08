using SerialPorts
using ArduinoTools

ser=connectBoard(115200)
k=0
j=0
jlast=0
ilast=digiRead(ser,5)
DCMotorSetup(ser,3,1,9,10)   # Setup the DC motor of the interrupt
for s=1:1000
  DCMotorRun(ser,1,100)  # Rotate the motor of the interrupt
  i=digiRead(ser,5)   # Read the signals of the receiver
  if i!=ilast    # Motor is rotating
    if i==1    # Condition when the receiver receives signal from transmitter
      j=j+1
    end
    sleep(0.01)
  end
  ilast=i
  if j!=jlast
    println(j)
    if j%17==0 && j!=0   # Condition for one complete rotation of the motor
      k=k+1  # Prints the no of rotations
      print(k)
      println("rotations completed")
    end
  end
  jlast=j
end
DCMotorRelease(ser,1)
close(ser)
