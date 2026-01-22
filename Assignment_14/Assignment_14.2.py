###################################################################################
#
#    Accept one number and return the cube of that number.
#
#####################################################################################

Cube = lambda No : (No * No * No)

def main():

    Value = 0
    Ret = 0

    print("Enter the number:")
    Value = int(input())

    Ret = Cube(Value)

    print("Cube of given number is:",Ret)


if __name__ == "__main__":
    main()