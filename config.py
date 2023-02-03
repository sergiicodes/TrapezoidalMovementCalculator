import numpy as np

#STANDARD TRAP FUNCTIONS 
class Standard_Y:
    
    #Y function for POSITION 
    def Y_Val_POS(xaxis1, time, max_velocity):
        
        m_list = [[(np.median(xaxis1))**2, np.median(xaxis1)], [time**2, time]]
        A = np.array(m_list)
        
        B = np.array([max_velocity, 0])
        X = np.linalg.inv(A).dot(B)
        
        quad_x = X[0]
        linear_x = X[1]
    
        Y_Concat_POS = ((quad_x/3)*(xaxis1**3)) + ((linear_x/2)*(xaxis1**2))
        
        return Y_Concat_POS
    
    
    #Y function for VELOCITY 
    def Y_Val_VEL(max_velocity):
        #the velocity increase:
        Yaccel = np.linspace(0,max_velocity,1100)
        #the dwell:
        Ydwell = [max_velocity for i in range(900)]
        #the veloctiy decrease:
        Ydecel = np.linspace(max_velocity, 0, 1100) 
        #this concatenates the prior arrays to make one, consolidated, final y-axis
        Y_Concat = np.concatenate((Yaccel, Ydwell, Ydecel))
        
        return Y_Concat
    
    
    #Y function for ACCELERATION 
    def Y_Val_ACCEL(max_velocity):
        #the velocity increase:
        Yaccel1 = [max_velocity for i in range(1100)]
        #the dwell:
        Ydwell1 = [0 for i in range(900)]
        #the veloctiy decrease:
        Ydecel1 = [-max_velocity for i in range(1100)]
        #this concatenates the prior arrays to make one, consolidated, final y-axis
        Y_Concat1 = np.concatenate((Yaccel1, Ydwell1, Ydecel1))

        return Y_Concat1

#----------------------------------------------------------------------------------------------

#CUSTOM TRAP FUNCTIONS 
class Custom_Y:
    
    #Y function for POSITION 
    def Y_Val_POS(xaxis2, time_of_move, peakVel):
        
        m_list = [[(np.median(xaxis2))**2, np.median(xaxis2)], [time_of_move**2, time_of_move]]
        A = np.array(m_list)
        
        B = np.array([peakVel, 0])
        X = np.linalg.inv(A).dot(B)
        
        quad_x = X[0]
        linear_x = X[1]
    
        Y_Concat_POS = ((quad_x/3)*(xaxis2**3)) + ((linear_x/2)*(xaxis2**2))
        
        return Y_Concat_POS
    
    #Y function for VELOCITY 
    def Y_Val_VEL(peakVel):
        #the velocity increase:
        Yaccel = np.linspace(0,peakVel,1100)
        #the dwell:
        Ydwell = [peakVel for i in range(900)]
        #the veloctiy decrease:
        Ydecel = np.linspace(peakVel, 0, 1100) 
        #this concatenates the prior arrays to make one, consolidated, final y-axis
        Y_Concat = np.concatenate((Yaccel, Ydwell, Ydecel))
        return Y_Concat
    
    #Y function for ACCELERATION 
    def Y_Val_ACCEL(peakVel):
        #the velocity increase:
        Yaccel1 = [peakVel for i in range(1100)]
        #the dwell:
        Ydwell1 = [0 for i in range(900)]
        #the veloctiy decrease:
        Ydecel1 = [-peakVel for i in range(1100)]
        #this concatenates the prior arrays to make one, consolidated, final y-axis
        Y_Concat1 = np.concatenate((Yaccel1, Ydwell1, Ydecel1))
        
        return Y_Concat1

#----------------------------------------------------------------------------------------------

class Tri_Y:
    
    #Y function for POSITION 
    def Y_Val_POS(xaxis2, time_of_move, peakVel):
        
        m_list = [[(np.median(xaxis2))**2, np.median(xaxis2)], [time_of_move**2, time_of_move]]
        A = np.array(m_list)
        
        B = np.array([peakVel, 0])
        X = np.linalg.inv(A).dot(B)
        
        quad_x = X[0]
        linear_x = X[1]
    
        Y_Concat_POS = ((quad_x/3)*(xaxis2**3)) + ((linear_x/2)*(xaxis2**2))
        
        return Y_Concat_POS
    
    #Y function for VELOCITY 
    def Y_Val_VEL(peakVel):
        #the velocity increase:
        Yaccel = np.linspace(0,peakVel,11)
        #the dwell:
        Ydwell = [peakVel for i in range(9)]
        #the veloctiy decrease:
        Ydecel = np.linspace(peakVel, 0, 11) 
        #this concatenates the prior arrays to make one, consolidated, final y-axis
        Y_Concat = np.concatenate((Yaccel, Ydwell, Ydecel))
        
        return Y_Concat
    
    #Y function for ACCELERATION 
    def Y_Val_ACCEL(peakVel):
        #the velocity increase:
        Yaccel1 = [peakVel for i in range(11)]
        #the dwell:
        Ydwell1 = [0 for i in range(9)]
        #the veloctiy decrease:
        Ydecel1 = [-peakVel for i in range(11)]
        #this concatenates the prior arrays to make one, consolidated, final y-axis
        Y_Concat1 = np.concatenate((Yaccel1, Ydwell1, Ydecel1))
        
        return Y_Concat1
