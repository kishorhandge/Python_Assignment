##############################################################################
#
# Write a program which contains one lambda function
# which accepts two parameters and returns its multiplication.
#
# Input  : 4  3
# Output : 12
#
# Input  : 6  3
# Output : 18
#
##############################################################################


Multi = lambda No1, No2 : (No1 * No2)
    
def main():

    No1 = 0
    No2 = 0
    Ret = 0
    
    print("Enter the  first number:")
    No1 = int(input())

    print("Enter the second number:")
    No2 = int(input())

    Ret = Multi(No1,No2)

    print("Multiplication of 2 number is :",Ret)


if __name__ == "__main__":
    main()