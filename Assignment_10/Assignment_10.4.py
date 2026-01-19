############################################################################
#
#       Write a program that accepts one number
#       and prints all even numbers till that number.
#       Input  : 10
#       Output : 2 4 6 8 10
#
#############################################################################

def DisplayEven(Value):
    
    i = 1
    while i <= Value:
        if i % 2 == 0:
            print(i, end=" ")
        i += 1


def main():

    print("Enter the number:")
    No = int(input())

    DisplayEven(No)


if __name__ == "__main__":
    main()
