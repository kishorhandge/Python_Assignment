############################################################################
#
#       Write a program that accepts one number
#      and prints the reverse of that number.
#      Input  : 123
#      Output : 321
#
#############################################################################

def PrintReverse(Value):
     
    Digit = 0

    while(Value != 0):
        Digit = Value % 10
        print(Digit)
        Value = Value // 10
     

def main():

    No = 0
    
    print("Enter the number:")
    No = int(input())

    PrintReverse(No)

if __name__ == "__main__":
    main()
