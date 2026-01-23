
##############################################################################
#
# Create a module named Arithmetic which contains four functions:
# Add() for addition, Sub() for subtraction,
# Mult() for multiplication and Div() for division.
# All functions accept two parameters as numbers
# and perform the respective operation.
# Write a Python program which calls all the functions
# from the Arithmetic module by accepting parameters from user.
#
##############################################################################

import Arithematic

            
def main():

    Value1 = 0
    Value2 = 0

    print("Enter the first name")
    Value1 = int(input())

    print("Enter the second name")
    Value2 = int(input())

    Ret = Arithematic.Addition(Value1,Value2)
    print("Addition is:",Ret)

    Ret = Arithematic.Substraction(Value1,Value2)
    print("Substraction is:",Ret)

    Ret = Arithematic.Division(Value1,Value2)
    print("Division is:",Ret)

if __name__ == "__main__":
    main()