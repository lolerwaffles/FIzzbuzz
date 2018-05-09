from random import *
import time, os

os.system('cls')
print("FizzBuzz with random number generation. Numbers are indicated to show program effectiveness\nCTRL+c to exit")

while True:
    number = int(random() * 100)
    fizzbuzz = ''
    if number % 3 == 0:
        fizzbuzz += 'fizz'
    if number % 5 == 0:
        fizzbuzz += 'buzz'
    print("{}    {}        ".format(number,fizzbuzz), end='\r')
    time.sleep(0.5)
