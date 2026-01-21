############################################################################
#
#      Write a program that accepts one number
#      and checks whether it is a perfect number or not.
#      Input  : 6
#      Output : Perfect Number
#
#############################################################################

def CheckPerfect(Value):
    
    Sum = 0

    for i in range(1,Value):
        if(Value % i == 0):
            Sum = Sum + i

    if(Sum == Value):
        print("It is Perfect Number:")

    else:
        print("It is not a Perfect Number:")
     

def main():
    
    No1 = 0

    print("Enter the number:")
    No1 = int(input())

    CheckPerfect(No1)

if __name__ == "__main__":
    main()
