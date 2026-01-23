
##############################################################################
#
# Write a program which accepts a number from user
# and returns the number of digits in that number.
#
##############################################################################


def Digit(No):

    Digit = 0
    Count = 0
    
    while(No != 0):
        Digit = No % 10
        Count = Count + 1
        No = No // 10

    print("Number of Digit in this Number are:",Count)

def main():

    Value = 0
    Ret = 0

    print("Enter the number")
    Value = int(input())

    Digit(Value)

if __name__ == "__main__":
    main()