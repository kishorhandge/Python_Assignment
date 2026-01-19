############################################################################
#
#       Write a program that accepts one number
#      and prints the sum of digits of that number.
#      Input  : 123
#      Output : 6
#
#############################################################################

def SumDigit(Value):
    Sum = 0
    Digit = 0

    while(Value != 0):
        Digit = Value % 10
        Sum = Sum + Digit
        Value = Value // 10

    print("Sum of Digit is:",Sum)
     

def main():

    print("Enter the number:")
    No = int(input())

    SumDigit(No)

if __name__ == "__main__":
    main()
