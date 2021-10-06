# Markhus Dammar
# 6 October 2021
# THis program will calculate the factorial of a number using different logic

myNumber = int(input("Please input a number to calculate its factorial >>> "))


def computeFactorial(myNumber):
    factorial = 1
    for digit in range(1, myNumber + 1):
        factorial = factorial * digit
    print(f"The factorial of {myNumber} is {factorial}")

computeFactorial(myNumber)
