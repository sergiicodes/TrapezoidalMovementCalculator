#Import Libraries 
import matplotlib.pyplot as plt
import numpy as np

#The functions for the Y axes on a seperate Python program and then importing the modules
from config import Standard_Y as sy  
from config import Custom_Y as cy 
from config import Tri_Y as ty 

#Displays Menu 
print("Standard or Custom Trap Move?\n")
ans = input("a - Standard\n b - Custom Trap\n  c - Triangle\n\nSelect: ")

#------------------------------------------------------------------------------

#STANDARD TRAP
if ans == "Standard" or ans=="standard" or ans=="a":

    #These are the inputs
    distance = float(input("Distance in Inches: "))
    time = float(input("Time in seconds: "))
    max_velocity = ((1.5*distance)/time)

    
    '''X'''
    #This will populate the x-axis, or the time
    xaxis1 = np.linspace(0,time,3100)
    
    '''The next arrays will populate the y-axis: position, velocity, and acceleration.
    Recall that a trap move consists of an increase in velocity, dwell (constant vel),
    and a decrease in velocty''' 
    
    '''Y'''
    yaxis1POS = sy.Y_Val_POS(xaxis1, time, max_velocity)
    yaxis1VEL = sy.Y_Val_VEL(max_velocity)
    yaxis1ACCEL = sy.Y_Val_ACCEL(max_velocity)
    
    #----------- SETS UP MULTI AXIS LABELS --------------
    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        for sp in ax.spines.values():
            sp.set_visible(False)
    
    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)
    
    par1 = host.twinx()
    par2 = host.twinx()
    
    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    par2.spines["right"].set_position(("axes", 1.2))
    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    make_patch_spines_invisible(par2)
    # Second, show the right spine.
    par2.spines["right"].set_visible(True)
    
    p1, = host.plot(xaxis1, yaxis1POS, "b-", label="Position")
    p2, = par1.plot(xaxis1, yaxis1VEL, "r-", label="Velocity")
    p3, = par2.plot(xaxis1, yaxis1ACCEL, "g-", label="Acceleration")
    
    host.set_xlabel("Time [s]")
    host.set_ylabel("Position [in]")
    par1.set_ylabel("Velocity [in/s]")
    par2.set_ylabel("Acceleration [in/$s^2$]")
    
    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())
    
    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)
    
    lines = [p1, p2, p3]
    
    #can un-comment this to get a legend, but I find it to clutter the screen 
    #host.legend(lines, [l.get_label() for l in lines])
    

    plt.grid(True, axis='both')
    plt.title("Standard Trap Move")
    plt.show()

#------------------------------------------------------------------------------

#CUSTOM TRAP    
elif ans == "Custom Trap" or ans=="custom trap" or ans=="custom" or ans=="b":
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
    Xaccel = np.linspace(0, accelTime/1000*900, 1000)
    XdwellTime = np.linspace(accelTime, accelTime + timeAtConstantVel, 1100)
    Xdecel = np.linspace(accelTime + timeAtConstantVel + decelTime/1000 ,time_of_move,1000)
         
    xaxis2 = np.concatenate((Xaccel, XdwellTime, Xdecel))
    
    '''The next arrays will populate the y-axis: position, velocity, and acceleration.
    Recall that a trap move consists of an increase in velocity, dwell (constant vel),
    and a decrease in velocty''' 
    
    '''Y'''    
    yaxis1POS = cy.Y_Val_POS(xaxis2, time_of_move, peakVel)
    yaxis1VEL = cy.Y_Val_VEL(peakVel)
    yaxis1ACCEL = cy.Y_Val_ACCEL(peakVel)
    
    #----------- SETS UP MULTI AXIS LABELS --------------

    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        for sp in ax.spines.values():
            sp.set_visible(False)

    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()

    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    par2.spines["right"].set_position(("axes", 1.2))
    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    make_patch_spines_invisible(par2)
    # Second, show the right spine.
    par2.spines["right"].set_visible(True)

    p1, = host.plot(xaxis2, yaxis1POS, "b-", label="Position")
    p2, = par1.plot(xaxis2, yaxis1VEL, "r-", label="Velocity")
    p3, = par2.plot(xaxis2, yaxis1ACCEL, "g-", label="Acceleration")

    host.set_xlabel("Time [s]")
    host.set_ylabel("Position [in]")
    par1.set_ylabel("Velocity [in/s]")
    par2.set_ylabel("Acceleration [in/$s^2$]")

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)

    lines = [p1, p2, p3]

    #can un-comment this to get a legend, but I find it to clutter the screen 
    #host.legend(lines, [l.get_label() for l in lines])

    plt.grid(True, axis='both')
    plt.title("Custom Trap Move")
    plt.show()
    
#------------------------------------------------------------------------------

#TRIANGLE    
elif ans == "Triangle" or ans=="triangle" or ans == "c":
    peakVel = float(input("Peak Velocity in in/s: "))
    distance2 = float(input("Distance in Inches: "))
    accel = float(input("Acceleration in in/s^2: "))
    
    #time it takes to complete the entire trap move
    time_of_move = (2*distance2)/peakVel
    
    decel = accel*peakVel/(accel*time_of_move-peakVel)
        
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
    yaxis1POS = ty.Y_Val_POS(xaxis2, time_of_move, peakVel)
    yaxis1VEL = ty.Y_Val_VEL(peakVel)
    yaxis1ACCEL = ty.Y_Val_ACCEL(peakVel)
    
    
    #----------- SETS UP MULTI AXIS LABELS --------------
    def make_patch_spines_invisible(ax):
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        for sp in ax.spines.values():
            sp.set_visible(False)
    
    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)
    
    par1 = host.twinx()
    par2 = host.twinx()
    
    # Offset the right spine of par2.  The ticks and label have already been
    # placed on the right by twinx above.
    par2.spines["right"].set_position(("axes", 1.2))
    # Having been created by twinx, par2 has its frame off, so the line of its
    # detached spine is invisible.  First, activate the frame but make the patch
    # and spines invisible.
    make_patch_spines_invisible(par2)
    # Second, show the right spine.
    par2.spines["right"].set_visible(True)
    
    p1, = host.plot(xaxis2, yaxis1POS, "b-", label="Position")
    p2, = par1.plot(xaxis2, yaxis1VEL, "r-", label="Velocity")
    p3, = par2.plot(xaxis2, yaxis1ACCEL, "g-", label="Acceleration")
    
    host.set_xlabel("Time [s]")
    host.set_ylabel("Position [in]")
    par1.set_ylabel("Velocity [in/s]")
    par2.set_ylabel("Acceleration [in/$s^2$]")
    
    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())
    
    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)
    
    lines = [p1, p2, p3]
    
    #can un-comment this to get a legend, but I find it to clutter the screen 
    #host.legend(lines, [l.get_label() for l in lines])
    
    plt.grid(True, axis='both')
    plt.title("Custom Triangle Move")
    plt.show()
