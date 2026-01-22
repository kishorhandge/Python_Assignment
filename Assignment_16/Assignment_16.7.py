
##############################################################################
#
# Write a program which contains one function that accepts one number
# from user and returns True if the number is divisible by 5,
# otherwise returns False.
#
##############################################################################


def CheckDivisible(No):
     
    if(No%5 == 0):
        return True
    else:
        return False
            
def main():

    Value = 0
    Ret = False

    print("Enter the number")
    Value = int(input())

    Ret = CheckDivisible(Value)
    print(Ret)

if __name__ == "__main__":
    main()