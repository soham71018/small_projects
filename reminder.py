import time 
import pyttsx3 
import os

def beep():
    os.system('afplay /System/Library/Sounds/Funk.aiff')

reminder = input("Enter what kind of reminder do you want :")
minutes =  float(input("Enter how many minitues of reminder do you want :"))
seconds = minutes * 60
print(f"Ok ! I will remind you at that {minutes} moment.")

for _ in range (3):
    beep()
    time.sleep(0.5)

time.sleep(seconds)
engine = pyttsx3.init()
rate = engine.getProperty('rate')   
engine.setProperty('rate', 110)  
engine.say(f"Hey Soham its time for your reminder of {reminder}", {reminder})
engine.runAndWait()
time.sleep(1)