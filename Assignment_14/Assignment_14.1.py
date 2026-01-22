###################################################################################
#
#   Accept one number and return the square of that number.
#
#####################################################################################

Square = lambda No : (No * No)

def main():

    Value = 0
    Ret = 0

    print("Enter the number:")
    Value = int(input())

    Ret = Square(Value)

    print("Square of given number is:",Ret)


if __name__ == "__main__":
    main()