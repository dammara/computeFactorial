# Markhus Dammar
# 6 October 2021
# THis program will calculate the factorial of a number

import math


def computeFactorial(myNumber):
    print(f'The factorial of {myNumber} is {math.factorial(myNumber)}')


myNumber = int(input("Please input a number to find the factorial. >>> "))
computeFactorial(myNumber)

