from tkinter import *
#import tkinter as tk
import math
#import time module
import time
import tkinter.messagebox


global count
count = 0
global timegap
timegap = 0
global time
Time = 0
global R
R=0
global S
S=0
global Q
Q=0



def calculate():
    try:
        global height
        height=str(entryheight.get())
        global weight
        weight=str(entryweight.get())
        global num_of_rev
        num_of_rev=int(entryNumofrev.get())
        global radius
        radius=str(entryradius.get())
    except:
        tkinter.messagebox.showinfo('WRONG INPUT',"Enter the value correctly,Don't type spaces after the value")
        print("PLease Enter the values correctly with the unit, EX: 8 cm")
        global count
        count = 1
    
    
    if count == 0:
        now_time = time.time()
        global timegap
        global Time
        Time = (now_time - start_time)
        timeduration = Time + timegap
        time_in_min= timeduration /60
        l1.config(text=round(timeduration,0))
        #calculate speed
        
        speed = float(get_speed(radius,num_of_rev))/60
        speed = round(speed,2)
        
        
        #calculate distance
        distance = get_distance(time_in_min,radius,num_of_rev)
        distance = round(distance, 2)
        #calculate calories
        calories= get_calories(weight,time_in_min,radius,num_of_rev)
        calories = round(calories, 2)
        #calcluate steps 
        steps = get_steps(height,time_in_min,radius,num_of_rev)
        steps = int(steps)
        
               
        labelspeed.config(text=speed)
        labeldistance.config(text=distance)
        labelcalories.config(text=calories)
        labelsteps.config(text=steps) 
        
        
        l1.after(1000,calculate)
        
    elif count == 1:
        
        print("End")
        #l1.config(text="Goo")

def stop():
    global count
    count= 1
    global timegap
    global Time
    timegap = timegap + Time
       
def starter():
    try:
        global count
        count= 0
        global start_time
        start_time=time.time()
        calculate()
        m()
       
        
    except:
        tkinter.messagebox.showinfo('NO INPUT',"First Enter the values")
        print("PLease Enter the values correctly with the unit")
        count = 1
    
def reset():
    global count
    count=1
    
    global height
    height=0
    Height.set('0')
    global weight
    weight=0
    Weight.set('0')
    global num_of_rev
    num_of_rev =0
    Numofrev.set('0')
    global radius
    radius = 0
    Radius.set('0')
    global Time
    Time = 0
    global timegap
    timegap =0
    speed = 0
    distance = 0
    calories = 0
    steps = 0
    labelspeed.config(text=speed)
    labeldistance.config(text=distance)
    labelcalories.config(text=calories)
    labelsteps.config(text=steps)  
    l1.config(text=Time) 

        
        
def convertionQ(value):
    '''
    A function to convert units
    '''
    try:
       
        
        global Q
    
        #convert height into meter
        if  Q==1:
        #1 cm = 1/100 m
            value=float(value)
            return value
            
        elif Q==2:
            value=float(value)*(1/100)
            return value
            
        elif Q==3:
        #1 in = 0.0254 m
            value=float(value)*0.0254
            return value
        
        else:
            #global count
            #count= 1
            tkinter.messagebox.showinfo('NO UNITS',"Enter the units")
            
    except:
        #x=0
        tkinter.messagebox.showinfo('NO UNITS',"Enter the units")
        
def convertionR(value):
    '''
    A function to convert units
    '''
    global R
    if  R==1:
        #1 cm = 1/100 m
        value=float(value)
        return value

    elif R==2:
        value=float(value)*(1/100)
        return value
        
    elif R==3:
        #1 in = 0.0254 m
        value=float(value)*0.0254
        return value
    
def convertionS(value):
    '''
    A function to convert units
    '''
    global S
        #convert weight into kg
    if S==1:
        value=float(value)
        return value
    elif S==2:
        #1 lb = 0.453592 kg
        value=float(value)*(1/1000)
        return value
    elif S==3:
        #1 lb = 0.453592 kg
        value=float(value)*0.453592
        return value
        
        
def get_speed(radius,num_of_rev):
    '''
     A function to calculate the speed of the treadmill in meter/min
     >>>get_speed(0.1,5)
     3.14
    '''
    #using convertion function
    radius= float(convertionQ(radius))
    return (2*math.pi*radius*num_of_rev)

def get_distance(time,radius,num_of_rev):
    '''
     A function to calculate the distance walked/ran on treadmill in meter
     >>>get_distance(30)
     94.2
    '''
    return  (float(time)*get_speed(radius,num_of_rev))
    
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
        
    
    weight = float(convertionS(weight))
    #get the L of oxygen consumed in L
    O2_consumed=((float(vo2)/1000)*float(weight)*time)
    #1L oxygen consumed = burning 5000cal
    cal_burnt=float(O2_consumed)*5000
    return (cal_burnt)

def get_steps(height,time,radius,num_of_rev):
    '''
     A function to get the number of steps taken
    '''
    height = float(convertionR(height))
    #get the common stride length for both male and female
    stride_length=height*((0.413+0.415)/2)
    #stride length=2 steps
    One_step = stride_length/2
    #calculate the number of steps taken
    num_of_steps = get_distance(time,radius,num_of_rev)/One_step
    return (num_of_steps)

def m():
    global R
    R =0
    global S
    S=0
    global Q
    Q=0
    
    Q = q.get()
    R = r.get()
    S = s.get()

dis = Tk()
dis.title("Tredmill Display-G108")
dis.geometry('750x450') 
#dis.configure(background = 'green')
#tkinter.messagebox.showinfo('WELCOME',"Enter the value and the unit 'Ex:4 cm',Don,t type spaces after the unit")

##### Output labels
l1=Label(dis,font="times 20",justify ='center')
l1.grid(row=2,column=1,columnspan=5)
l2=Label(dis,font="times 20")
l2.grid(row=2,column=4)
labelspeed=Label(dis,fg='green',font=('Times New Roman',20,'bold'),width =8)
labelspeed.grid(row=9,column=1)
labeldistance=Label(dis,fg='green',font=('Times New Roman',20,'bold'),width =8)
labeldistance.grid(row=11,column=1)
labelcalories=Label(dis,fg='green',font=('Times New Roman',20,'bold'),width =15)
labelcalories.grid(row=11,column=2)
labelsteps=Label(dis,fg='green',font=('Times New Roman',20,'bold'),width =8)
labelsteps.grid(row=11,column=3,columnspan=5)

labelspeedo=Label(dis,text='Speed (m/s)',bg= 'powder blue',fg='blue',font=('Times New Roman',20,'bold'),width =15)
labelspeedo.grid(row=10,column=1)
labeldistanceo=Label(dis,text='Distance (m)',bg= 'powder blue',fg='blue',font=('Times New Roman',20,'bold'),width =15)
labeldistanceo.grid(row=12,column=1)
labelcalorieso=Label(dis,text='Calories (J)',bg= 'powder blue',fg='blue',font=('Times New Roman',20,'bold'),width =15)
labelcalorieso.grid(row=12,column=2)
labelstepso=Label(dis,text='Steps Count',bg= 'powder blue',fg='blue',font=('Times New Roman',20,'bold'),width =15)
labelstepso.grid(row=12,column=3,columnspan=5)


#### input labels =========================================
labelheight=Label(dis,text='Height',fg='green',font=('Times New Roman',20,'bold'))
labelheight.grid(row=3,column=1)
labelweight=Label(dis,text='Weight',fg='green',font=('Times New Roman',20,'bold'))
labelweight.grid(row=4,column=1)
labelnumofrev=Label(dis,text='Num:of Rev',fg='green',font=('Times New Roman',20,'bold'))
labelnumofrev.grid(row=5,column=1)
labelradius=Label(dis,text='Radius',fg='green',font=('Times New Roman',20,'bold'))
labelradius.grid(row=6,column=1)

#####Radiobuttons=========================================
r= IntVar()
r1=Radiobutton(dis,text="m  ",font=('Times New Roman',15,'bold'),variable=r, value=1,command =m)
r1.grid(row=3,column=3)
r2=Radiobutton(dis,text="cm ",font=('Times New Roman',15,'bold'),variable=r, value=2,command =m)
r2.grid(row=3,column=4)
r3=Radiobutton(dis,text="in",font=('Times New Roman',15,'bold'),variable=r, value=3,command =m)
r3.grid(row=3,column=5)
#########
s= IntVar()
r4=Radiobutton(dis,text="kg",font=('Times New Roman',15,'bold'),variable=s, value=1,command =m)
r4.grid(row=4,column=3)
r5=Radiobutton(dis,text="g",justify ='left',font=('Times New Roman',15,'bold'),variable=s, value=2,command =m)
r5.grid(row=4,column=4)
r6=Radiobutton(dis,text="lb",font=('Times New Roman',15,'bold'),variable=s, value=3,command =m)
r6.grid(row=4,column=5)
##########
q= IntVar()
r7=Radiobutton(dis,text="m  ",font=('Times New Roman',15,'bold'),variable=q, value=1,command =m)
r7.grid(row=6,column=3)
r8=Radiobutton(dis,text="cm ",justify ='center',font=('Times New Roman',15,'bold'),variable=q, value=2,command =m)
r8.grid(row=6,column=4)
r9=Radiobutton(dis,text="in",font=('Times New Roman',15,'bold'),variable=q, value=3,command =m)
r9.grid(row=6,column=5)

##### Entry text boxes====================================
Height=StringVar()
entryheight=Entry(dis,bd=4,textvariable=Height,justify ='center',font=('Times New Roman',20), width =10)
entryheight.grid(row=3,column=2)
Weight=StringVar()
entryweight=Entry(dis,bd=4,textvariable=Weight,justify ='center',font=('Times New Roman',20), width =10)
entryweight.grid(row=4,column=2)
Numofrev=StringVar()
entryNumofrev=Entry(dis,bd=4,textvariable=Numofrev,justify ='center',font=('Times New Roman',20), width =10)
entryNumofrev.grid(row=5,column=2)
Radius=StringVar()
entryradius=Entry(dis,bd=4,textvariable=Radius,justify ='center',font=('Times New Roman',20), width =10)
entryradius.grid(row=6,column=2)

##buttons======================================================
    

b2=Button(dis,padx=16,bd=8, fg='black',font=('Times New Roman',10,'bold'), bg= 'powder blue',text="START",width=10,command=starter)
b2.grid(row=8,column=1)

b3=Button(dis,padx=16,bd=8, fg='black',font=('Times New Roman',10,'bold'), bg= 'powder blue',text="STOP",width=10,command=stop)
b3.grid(row=8,column=2)

b4=Button(dis,padx=16,bd=8, fg='black',font=('Times New Roman',10,'bold'), bg= 'powder blue',text="RESET",width=10,command=reset)
b4.grid(row=8,column=3,columnspan=5)


dis.mainloop()
