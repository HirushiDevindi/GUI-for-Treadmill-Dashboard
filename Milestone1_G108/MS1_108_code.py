# To run program with custom parameters
# python E18_G_108.py --motor 4 --radius "0.09 m" --height "170 cm" --time "600 s" --weight "100 lb"

# To run program with default parameters
# python E18_G_108.py

import argparse

#import the math module 
import math


'''
A set of functions to calculate,

 speed
 distance walked/ran
 calories burnt
 number of steps taken

while running or walking on a treadmill 
'''

def convertion(inputs):
    '''
    A function to convert units
    '''
    value,unit=inputs.split(' ')
    #convert height into meter
    if unit=='cm':
    #1 cm = 1/100 m
       value=float(value)*(1/100)
       return value
    elif unit=='in':
    #1 in = 0.0254 m
        value=float(value)*0.0254
        return value
    #convert time into min
    elif unit=='s':
    #1 s = 1/60 min
        value=float(value)*(1/60)
        return value
    elif unit=='h':
    #1 h = 60 min
        value=float(value)*60
        return value
    #convert weight into kg
    elif unit=='lb':
    #1 lb = 0.453592 kg
        value=float(value)*0.453592
        return value
    else:
        value=float(value)
        return value

def get_speed(radius,num_of_rev):
    '''
     A function to calculate the speed of the treadmill in meter/min
     >>>get_speed(0.1,5)
     3.14
    '''
    #using convertion function
    radius= float(convertion(radius))
    return (2*math.pi*radius*num_of_rev)
     
def get_distance(time,radius,num_of_rev):
    '''
     A function to calculate the distance walked/ran on treadmill in meter
     >>>get_distance(30)
     94.2
    '''

    time = float(convertion(time))
    return  (time*get_speed(radius,num_of_rev))

def get_calories(weight,time,radius,num_of_rev):
    '''
     A function to calculate the calories burnt in cal
    '''
    
    grade=0.1#It is assumed that grade=10% since this is not given
    s=get_speed(radius,num_of_rev)
    
    #select the activity whether it is running or walking 
    if s > (3.7*26.82):
        #for running 
        #get the MET value in mL/kg/min
        vo2=(0.2*s)+(0.9*s*grade)+3.5
    else:
        #for walking
        #get the MET value in mL/kg/min
        vo2=(0.1*s)+(1.8*s*grade)+3.5
        
    time = float(convertion(time))
    weight = float(convertion(weight))
    #get the L of oxygen consumed in L
    O2_consumed=((float(vo2)/1000)*float(weight)*time)
    #1L oxygen consumed = burning 5000cal
    cal_burnt=float(O2_consumed)*5000
    return (cal_burnt)

        
def get_steps(height,time,radius,num_of_rev):
    '''
     A function to get the number of steps taken
    '''
    height = float(convertion(height))
    #get the common stride length for both male and female
    stride_length=height*((0.413+0.415)/2)
    #stride length=2 steps
    One_step = stride_length/2
    #calculate the number of steps taken
    num_of_steps = get_distance(time,radius,num_of_rev)/One_step
    return (num_of_steps)


#====================================================================================
# Don't change the the code below this point
if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--motor", type=int, dest="motor_rate", help="EXAMPLE: 3", default=3)
    args.add_argument("--radius", type=str, dest="radius", help="EXAMPLE: 8 cm", default="8 cm")
    args.add_argument("--weight", type=str, dest="weight", help="EXAMPLE: 50 kg", default="50 kg")
    args.add_argument("--height", type=str, dest="height", help="EXAMPLE: 63 in", default="63 in")
    args.add_argument("--time", type=str, dest="time", help="EXAMPLE: 1 h", default="1 h")
    
    args=args.parse_args()

# Don't change the the code above this point
#=========================================================================================   
    
    print(int(get_speed(args.radius,args.motor_rate)/60),'m/s')
    print(int(get_distance(args.time,args.radius,args.motor_rate)),'m')
    print(int(get_calories(args.weight,args.time,args.radius,args.motor_rate)),'cal')
    print(int(get_steps(args.height,args.time,args.radius,args.motor_rate)))
    
