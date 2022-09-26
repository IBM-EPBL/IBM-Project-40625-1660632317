# kumar A Team Member
#Assignment - 2
"""Build a python code, Assume u get temperature and humidity values generated with random function to a variable)
and write a condition to continuously detect alarm in case of high temperature."""


import random, time, winsound

while True:
    temp = random.randint(1,100)
    if temp > 60:
        print("Alert Temperature is high!!")
        winsound.PlaySound("beep-warning-6387.wav",winsound.SND_FILENAME)
    else:
        print("Temperature is Normal")
    
    time.sleep(1)
