# kumar A Team Member
# Assignment - 2
"""Build a python code, Assume u get temperature and humidity values generated with random function to a variable)
and write a condition to continuously detect alarm in case of high temperature."""

import random, time, winsound

while True:
    Temperature = random.randint(1,100)
    Humidity = random.randint(1,50)

    if((Temperature < 50) & (Humidity < 30)):
        print("Temperature is Normal!:",Temperature)
        print("Humidity is Normal!:",Humidity)
        print("Alarm off!")

    elif((Temperature < 50) & (Humidity >30)):
        print("Temperature is Normal!:",Temperature)
        print("Humidity is High!:",Humidity)
        print("Alarm off!")

    elif((Temperature > 50) & (Humidity < 30)):
        print("Temperature is High!:",Temperature)
        print("Humidity is Normal!:",Humidity)
        print("Alarm on!")
        winsound.PlaySound("beep-warning-6387.wav",winsound.SND_FILENAME)

    elif((Temperature > 50) & (Humidity > 30)):
        print("Temperature is High!:",Temperature)
        print("Humidity is High!:",Humidity)
        print("Alarm on!")
        winsound.PlaySound("beep-warning-6387.wav",winsound.SND_FILENAME)
    else:
        print("Temperature is Normal!:",Temperature)
        print("Humidity is Normal!:",Humidity)
        print("Alarm off!")
    
    
    time.sleep(1)
