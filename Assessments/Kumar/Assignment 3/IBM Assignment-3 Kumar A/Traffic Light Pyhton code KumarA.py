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