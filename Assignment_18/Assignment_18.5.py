##############################################################################
#
# Write a program which accepts N numbers from user
# and stores them into a list.
# Return the addition of all prime numbers from that list.
# Main Python file accepts N numbers from user
# and passes each number to ChkPrime() function,
# which is part of a user-defined module named MarvellousNum.
# Name of the function in main Python file should be ListPrime().
#
##############################################################################

from MarvellousNum import ChkPrime

def ListPrime(Arr):
    Sum = 0

    for i in Arr:
        if ChkPrime(i):
            Sum = Sum + i

    return Sum


def main():

    Result = list()

    print("Enter number of elements:")
    Size = int(input())

    print("Enter the elements:")
    for i in range(Size):
        No = int(input())
        Result.append(No)

    Ret = ListPrime(Result)
    print("Addition of prime numbers is:", Ret)


if __name__ == "__main__":
    main()