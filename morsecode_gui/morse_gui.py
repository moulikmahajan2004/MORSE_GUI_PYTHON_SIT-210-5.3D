import tkinter as tk
from gpiozero import LED
import RPi.GPIO as GPIO
import time
import atexit


##LED DECLRARATION
led = LED(14)																																																																																																																																																																																																																																																																																																																																																																																																																																																																
root = tk.Tk()
root.title("PYTHON FIRST GUI")

##variable

name = tk.StringVar()




  
## EVENT FUNCTION ##
def Bulub_high():
    root.after(1000,led.on())


def Bulub_low():
    root.after(500,led.off())
    
    
def Bulub_small_low():
    root.after(100,led.off())
    
    
def Bulub_small_high():
    root.after(100,led.on())
     
    
    
def print_name_func():
     for i in name:
         print(i)

def morse( nam):
    if nam =="A":
        Bulub_low()
        Bulub_high()
    if nam =="B":
        Bulub_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        
    if nam =="C":
        Bulub_high()
        Bulub_low()
        Bulub_high()
        Bulub_low()
        
    if nam =="D":
        Bulub_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        
    if nam =="E":
        Bulub_low()
    
          
    if nam =="F":
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_high()
        Bulub_low()
        
              
    if nam =="G":
        Bulub_high()
        Bulub_small_low()
        Bulub_high()
        Bulub_low()
        
              
    if nam =="H":
        
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        
        
              
    if nam =="I":
        Bulub_small_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        
        
              
    if nam =="J":
      
        Bulub_low()
        Bulub_high()
        Bulub_small_low()
        Bulub_high()
        Bulub_small_low()
        Bulub_high()
       
        
              
    if nam =="K":
        Bulub_high()
        Bulub_low()
        Bulub_high()
        
        
              
    if nam =="L":
        Bulub_low()
        Bulub_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
    
        
              

    if nam =="M":
       ## --
      Bulub_high()
      Bulub_small_low()
      Bulub_high()
              
    if nam =="N":
        Bulub_high()
        Bulub_low()
              
    if nam =="O":
        Bulub_high()
        Bulub_low()
        Bulub_high()
        Bulub_low()
        Bulub_high()
        
              
    if nam =="P":
        Bulub_low()
        Bulub_high()
        Bulub_small_low()
        Bulub_high()
        Bulub_low()
        
        
              
    if nam =="Q":
        Bulub_high()
        Bulub_small_low()
        Bulub_high()
        Bulub_low()
        Bulub_high()
        
              
    if nam =="R":
        Bulub_low()
        Bulub_high()
        Bulub_low()
        
              
    if nam =="S":
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        
        
        
              
    if nam =="T":
        Bulub_high()
        
              
    if nam =="U":
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_high()
        
        
              
    if nam =="V":
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_high()
              
    if nam =="W":
        Bulub_low()
        Bulub_high()
        Bulub_small_low()
        Bulub_high()
        
    if nam =="X":
        Bulub_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        Bulub_high()
           
    if nam =="Y":
        Bulub_high()
        Bulub_low()
        Bulub_high()
        Bulub_small_low()
        Bulub_high()
        
    if nam =="z":
        Bulub_high()
        Bulub_small_high()
        Bulub_high()
        Bulub_low()
        Bulub_small_high()
        Bulub_low()
        
def ledTOggle():
    
     ##print("THE NAME OF THE USER IS " - name)
     name = text_box.get("1.0","end-1c")
     print(name)
     
    
 ##printing the single chracter
     for i in name:
         morse(i.upper())

def CLOSE_GUI():
    root.destroy()
    
    
    
##widgets
text_box = tk.Text(root, height= 5, width = 60)
##text_box.grid(row =0,column = 1)
text_box.pack()

ledButton = tk.Button(root, text = "turn led on", command = ledTOggle, bg = 'bisque2' , height = 1 , width = 24)
##ledButton.grid(row = 0, column = 28)
ledButton.pack()

exitButton = tk.Button(root, text="EXIT WINDOW", command=CLOSE_GUI, bg='red', height = 1, width = 24)
##exitButton.grid(row=0, column=24)
exitButton.pack()

# Set the protocol for window closing
root.protocol("WM_DELETE_WINDOW", CLOSE_GUI)
root.mainloop()














