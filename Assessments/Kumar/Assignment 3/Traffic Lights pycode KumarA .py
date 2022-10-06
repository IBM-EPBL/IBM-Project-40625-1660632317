#IBM Assessment
#Assignment - 3
#Kumar A

#Write python code for blinking LED and Traffic Lights for Raspberry pi. Only pyhton code is enough,no need to excute in raspberry pi.

#Traffic Lights python code for Raspberry pi.
from GPIO.ZERO import LED

from time import sleep

red=LED(17)

yellow=LED(22)

green=LED(27)

while True:

    red.on()

    sleep(15)

    red.off()

    sleep(1)

    yellow.on()

    sleep(10)

    yellow.off()

    sleep(1)

    green.on()

    sleep(10)

    green.off()

    sleep(1)
