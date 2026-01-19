############################################################################
#
#       Write a program that accepts one number
#       and prints all odd numbers till that number.
#       Input  : 10
#       Output : 1 3 5 7 9
#
#############################################################################

def DisplayOdd(Value):
    
    i = 1
    while i <= Value:
        if i % 2 == 1:
            print(i, end=" ")
        i += 1


def main():

    print("Enter the number:")
    No = int(input())

    DisplayOdd(No)


if __name__ == "__main__":
    main()
