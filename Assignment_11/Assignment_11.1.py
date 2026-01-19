############################################################################
#
#       Write a program that accepts one number
#      and checks whether it is prime or not.
#      Input  : 11
#      Output : Prime Number
#
#############################################################################

def CheckPrime(Value):
    Count = 0

    for i in range(2,Value):
        if(Value % i == 0):
            Count = Count + 1
            break
        
    if(Count == 0):
        return True
    else:
        return False


def main():

    bRet = False

    print("Enter the number:")
    No = int(input())

    bRet = CheckPrime(No)

    if(bRet == True):
        print("It is Prime Number:")

    else:
         print("It Not a is Prime Number:")

if __name__ == "__main__":
    main()
