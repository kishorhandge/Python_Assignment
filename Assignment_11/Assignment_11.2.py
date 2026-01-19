############################################################################
#
#       Write a program that accepts one number
#      and prints the count of digits in that number.
#      Input  : 7521
#      Output : 4
#
#############################################################################

def CountDigit(Value):
    Count = 0
    Digit = 0

    while(Value != 0):
        Digit = Value % 10
        Count = Count + 1
        Value = Value // 10

    print("Count of Digit is:",Count)
     

def main():

    print("Enter the number:")
    No = int(input())

    CountDigit(No)

if __name__ == "__main__":
    main()
