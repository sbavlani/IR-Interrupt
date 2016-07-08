ok=open_serial(1,2,115200)   // At port 2 with baudrate 115200
if ok~=0 then error('Unable to open serial port.  Please check') end
jlast=0
k=0
j=0
ilast=cmd_digital_in(1,5)  
cmd_dcmotor_setup(1,3,1,9,10)  // DC motor setup
for s=1:5000
    cmd_dcmotor_run(1,1,100)  // Rotate the motor of the interrupt
    i=cmd_digital_in(1,5)   // Read the signal of the receiver of the IR sensor
    if (i~=ilast)  // Check the rotation of motor
        if (i==1) then
            j=j+1
        end
        sleep(10)
    end
    ilast=i
    if (j~=jlast)  // If the motor rotates 
        disp(j)   // Print the number of teeth on the gear
        if (modulo(j,17)==0 & j~=0) //  Condition for one complete rotation
            k=k+1
            disp(k, "rotations complete")  // No of rotations completed
        end
    end
    jlast=j
end
cmd_dcmotor_release(1,1)
close_serial(1)
