I work primarily with industrial robot arms. In the industry they are called "loaders", powered by servo motors. 
A phenomenom of interest is the velocity of the loader. Where there is velocity, one can also observe the position and acceleration of the arm as well.
A common path of travel by these loaders are called index "trap" moves, short for trapezoidal. 
Kinematically, a trap move consists of a linearly increasing for the initial third of the time, a "dwell" where the velocity is constant at a peak speed for the middle third of the time, and then a linearly decreasing velocity for the last third of the time.  
This index move does not have to be a symmetrical (custom trap) nor have a dwell time (triangle move)--as in the loader may increase in velocity and then suddenly decrease without staying a considerable amount of time at its peak velocity.
Here, I created a calculator of sorts that is designed to prompt the user to first input which of the index moves the user wants to model (standard trap, custom trap, triangle) and then calculate and visualize a plot of the position, velocity, and acceleration. 
