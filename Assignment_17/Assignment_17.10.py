
##############################################################################
#
# Write a program which accepts a number from user
# and returns the addition of digits in that number.
#
##############################################################################


def Digit(No):

    Digit = 0
    Sum = 0
    
    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    print("Addition of Digit is:",Sum)

def main():

    Value = 0
    Ret = 0

    print("Enter the number")
    Value = int(input())

    Digit(Value)

if __name__ == "__main__":
    main()