l =  ['15 Lunges and 20 Pushups ',  
      
    '20 Russian Twists and 1 minute Plank', 
           
    '40 Squats and 40 Crunches',
           
    '60 High Knees and 50 Deadlifts',

    '50 Mountiain Climbers and 30 Overhead Presses',
           
    '40 Reverse Crunches and 30 Burpees', 

    '30 Side Planks and 20 Supermans',
      
    '20 Jumping Jacks and 1 minute wall sit',

    '10 Sprawls and 10 Air Squats',

    '20 Leg Raises and 20 Leg Lift Crunches']

import random
from tkinter import *
gui=Tk()
gui.title("Workout Generator")
gui.geometry("200x200")
def printer():
    var=StringVar()
    var.set(random.choice(l))
    w2=Label(gui,textvariable=var, fg='red', bg='white')
    w2.pack()
btn=Button(gui,text="Your Workout", fg='blue', bg='white', command=printer)   
btn.pack()




 

