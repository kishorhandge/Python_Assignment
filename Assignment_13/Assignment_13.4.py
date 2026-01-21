############################################################################
#
#      Write a program that accepts one number
#      and prints the binary equivalent of that number.
#
#############################################################################

def BinaryEquivalent(Value):
    
    Binary = ""

    while Value > 0:
        Digit = Value % 2
        Binary = str(Digit) + Binary
        Value = Value // 2

    print("Binary Equivalent is:", Binary)


def main():
    
    No1 = 0

    print("Enter the number:")
    No1 = int(input())

    BinaryEquivalent(No1)

if __name__ == "__main__":
    main()
