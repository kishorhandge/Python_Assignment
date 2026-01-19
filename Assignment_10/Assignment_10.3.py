############################################################################
#
#       Write a program that accepts one number
#       and prints the factorial of that number.
#       Input  : 5
#       Output : 120
#
#############################################################################
 

def  Factorial(Value):
    
    Fact = 1
    i = 1
    while(i<=Value):
        Fact = Fact * i
        i = i + 1
    return Fact

def main():

    No = 0
    Ret = 0
 
    print("Enter the number")
    No = int(input())

    Ret = Factorial(No)

    print("Factorial is :",Ret)


if __name__ == "__main__":
    main()

