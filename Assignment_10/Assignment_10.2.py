############################################################################
#
#       Write a program that accepts one number
#       and prints the sum of first N natural numbers.
#       Input  : 5
#       Output : 15
#
#############################################################################
 

def  Natural(Value):
    Sum = 0
    i = 0
    while(i<=Value):
        Sum = Sum + i
        print(Sum)
        i = i + 1
     

def main():

    No = 0
 
    print("Enter the number")
    No = int(input())

    Natural(No)


if __name__ == "__main__":
    main()

