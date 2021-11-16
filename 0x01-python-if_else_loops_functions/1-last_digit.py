#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
msg = "last digit of {:d} is {:d} and is"
if (number < 0 and ld != 0):
    ld = -(10 - ld)
if (ld > 5):
    print("{:s} greater than 5".format(msg).format(number, ld))
elif (ld < 6 and ld != 0):
    print("{:s} less than 6 and not 0".format(msg).format(number, ld))
elif (ld == 0):
    print("{:s} 0".format(msg).format(number, ld))
