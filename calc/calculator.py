# Simple calculator
# 2018.11.23

import os

'''
Write a calculator script that waits for the user to enter a number, 
then a sign (plus, minus, multiplication and division), 
then a number again. After the 2nd number input, 
the script should calculate the addition or subtraction and print it out.
Then the program should run again with asking for the first number.

The script should exit when the user enters a letter instead of a number.

Submit your python script file.
'''


def add(number1, number2):
    result_add = int(number1) + int(number2)
    return result_add


def divede(number1, number2):
    result_div = int(number1) / int(number2)
    if number2 == 0:
        return ZeroDivisionError
    else:
        return result_div


def subtraction(number1, number2):
    result_sub = int(number1) - int(number2)
    return result_sub


def multiply(number1, number2):
    result_mul = int(number1) * int(number2)
    return result_mul


def main():
    while True:
        fistnumber = input("Please enter a number: ")
        operator = input("Please choose an operator(| + | / | - | * |): ")
        secondnumber = input("Please enter a number: ")
        if operator == '+':
            print(fistnumber, '+', secondnumber, '=', add(fistnumber, secondnumber))
        elif operator == '/':
            print(fistnumber, '/', secondnumber, '=', divede(fistnumber, secondnumber))
        elif operator == '-':
            print(fistnumber, '-', secondnumber, '=', subtraction(fistnumber, secondnumber))
        elif operator == '*':
            print(fistnumber, '*', secondnumber, '=', multiply(fistnumber, secondnumber))
        else:
            break


if __name__ == "__main__":
    main()
