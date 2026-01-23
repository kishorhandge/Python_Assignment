##############################################################################
#
# Write a program which contains one lambda function
# which accepts one parameter and returns power of two.
#
# Input  : 4
# Output : 16
#
# Input  : 6
# Output : 64
#
##############################################################################

PowerOfTwo = lambda No : (2 ** No)
    
def main():

    No = 0
    Ret = 0
    
    print("Enter the number:")
    No = int(input())

    Ret = PowerOfTwo(No)

    print("Power of 2 of given number is :",Ret)


if __name__ == "__main__":
    main()