#######################################################################
#       Write a program that accepts one number
#       and checks whether it is divisible by 3 and 5.
#       Input  : 15
#       Output : Divisible by 3 and 5
#
######################################################################


def  CheckDivisible(Value):
    
    if(Value % 3 == 0 and Value % 5 == 0):
        return True
    else:
        False
     

def main():

    No = 0
    bRet = False
 
    print("Enter the number")
    No = int(input())

    bRet = CheckDivisible(No)

    if(bRet == True):
        print("Number is divisible:")
    else:
        print("Number is not divisible:")
    

if __name__ == "__main__":
    main()

