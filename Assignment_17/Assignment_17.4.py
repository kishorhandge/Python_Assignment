
##############################################################################
#
# Write a program which accepts one number from user
# and returns the addition of its factors.
#
##############################################################################


def AdditionFactors(No):
     
    Total = 0

    for i in range(1,No + 1):
        if(No%i == 0):
            Total = Total + i

    return Total
         
def main():

    Value = 0
    Ret = 0

    print("Enter the number")
    Value = int(input())

    Ret = AdditionFactors(Value)
    print("Addition of Factor is:",Ret)

if __name__ == "__main__":
    main()