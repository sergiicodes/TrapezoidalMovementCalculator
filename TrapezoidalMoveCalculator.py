import numpy as np
import matplotlib.pyplot as plt


print("Standard or Custom Trap Move?\n")
ans = input("a - Standard\n b- Custom Trap\n  c - Triangle\n\nSelect: ")

if ans == "Standard" or ans=="a":
    
    #These are the inputs
    distance = float(input("Distance in Inches: "))
    time = float(input("Time in seconds: "))
    max_velocity = ((1.5*distance)/time)
    
    '''X'''
    #This will populate the x-axis, or the time
    xaxis1 = np.linspace(0,time,31)
    
    '''The next arrays will populate the y-axis, the velocity in inches per second.
    Recall that a trap move consists of an increase in velocity, dwell (constant vel),
    and a decrease in velocty''' 
    
    '''Y'''
    #the velocity increase:
    Yaccel = np.linspace(0,max_velocity,11)
    #the dwell:
    Ydwell = [max_velocity for i in range(9)]
    #the veloctiy decrease:
    Ydecel = np.linspace(max_velocity, 0, 11)
    
    #this concatenates the prior arrays to make one, consolidated, final y-axis
    yaxis1 = np.concatenate((Yaccel, Ydwell, Ydecel))
    
    '''Plots'''
    plt.plot(xaxis1, yaxis1, color="green")
    plt.grid(True)
    plt.xlabel("Time [s]")
    plt.ylabel("Velocity [in/s]")
    plt.title("Standard Trap Move")
    plt.show()

elif ans == "Custom Trap" or ans=="b":
    accel = float(input("Acceleration in in/s^2: "))
    decel = float(input("Deceleration in in/s^2: "))
    peakVel = float(input("Peak Velocity in in/s: "))
    distance2 = float(input("Distance in Inches: "))
    
    #time it takes to complete the entire trap move
    time_of_move = distance2/peakVel+(peakVel/2)*(1/abs(decel)+1/abs(accel))
    #These are other calculations that are specific to the Custom Trap Move
    customTrapValue = time_of_move - peakVel/decel
    accelTime = peakVel / accel
    decelTime = time_of_move - customTrapValue
    timeAtConstantVel = customTrapValue - accelTime
        
    '''X'''
    #This will populate the x-axis, or the time
    Xaccel = np.linspace(0, accelTime/10*9, 10)
    XdwellTime = np.linspace(accelTime, accelTime + timeAtConstantVel, 11)
    Xdecel = np.linspace(accelTime + timeAtConstantVel + decelTime/10 ,time_of_move,10)
         
    xaxis2 = np.concatenate((Xaccel, XdwellTime, Xdecel))

    
    '''The next arrays will populate the y-axis, the velocity in inches per second.
    Recall that a trap move consists of an increase in velocity, dwell (constant vel),
    and a decrease in velocty''' 
    
    '''Y'''
    #the velocity increase:
    Yaccel2 = np.linspace(0,peakVel,11)
    #the dwell:
    Ydwell2 = [peakVel for i in range(9)]
    #the veloctiy decrease:
    Ydecel2 = np.linspace(peakVel, 0, 11)
    
    #this concatenates the prior arrays to make one, consolidated, final y-axis
    yaxis2 = np.concatenate((Yaccel2, Ydwell2, Ydecel2))
    
    '''Plots'''
    plt.plot(xaxis2, yaxis2, color="red")
    plt.grid(True)
    plt.xlabel("Time [s]")
    plt.ylabel("Velocity [in/s]")
    plt.title("Custom Trap Move")
    plt.show()
    
elif ans == "Triangle" or ans == "c":
    peakVelTri = float(input("Peak Velocity in in/s: "))
    distanceTri = float(input("Distance in Inches: "))
    accelTri = float(input("Acceleration in in/s^2: "))
    
    #time it takes to complete the entire triangle move
    time_of_moveTri = 2*distanceTri/peakVelTri
    
    decel2 = accelTri*peakVelTri/(accelTri*time_of_moveTri-peakVelTri)
    
    #These are other calculations that are specific to the triangle Move
    customTrapValue2 = time_of_moveTri - peakVelTri/decel2
    accelTimeTri = peakVelTri / accelTri
    decelTimeTri = time_of_moveTri - customTrapValue2
    timeAtConstantVel2 = customTrapValue2 - accelTimeTri
    
    '''X'''
    #This will populate the x-axis, or the time
    XaccelTRI = np.linspace(0, accelTimeTri/10*9, 10)
    XdwellTimeTRI = np.linspace(accelTimeTri, accelTimeTri + timeAtConstantVel2, 11)
    XdecelTRI = np.linspace(accelTimeTri + timeAtConstantVel2 + decelTimeTri/10 ,time_of_moveTri,10)
         
    #this concatenates the prior arrays to make one, consolidated, final y-axis
    xaxisTRI = np.concatenate((XaccelTRI, XdwellTimeTRI, XdecelTRI))
    print("Time [s] data points: ", xaxisTRI)
    print(f"Has {len(xaxisTRI)} data points")


    '''Y'''
    #the velocity increase:
    YaccelTRI = np.linspace(0, (accelTimeTri/10*9)*accelTri ,10)
    #the dwell:
    YdwellTRI = [peakVelTri for i in range(11)]
    #the veloctiy decrease:
    YdecelTRI = np.linspace(peakVelTri - decel2*(XdecelTRI[0] - accelTimeTri), 0, 10)
    
    #this concatenates the prior arrays to make one, consolidated, final y-axis
    yaxisTRI = np.concatenate((YaccelTRI, YdwellTRI, YdecelTRI))
    print("Velocity [in/s] data points: ", yaxisTRI)
    print(f"Has {len(xaxisTRI)} data points")
    
    
    '''Plots'''
    plt.plot(xaxisTRI, yaxisTRI, color="blue")
    plt.grid(True)
    plt.xlabel("Time [s]")
    plt.ylabel("Velocity [in/s]")
    plt.title("Triangle Move")
    plt.show()
