###################################################################################
#
#     Accept two numbers and return their multiplication.
#
#####################################################################################

Multiplication = lambda No1 ,No2  :( No1 * No2)


def main():

    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the First number:")
    Value1 = int(input())

    print("Enter the  Second number:")
    Value2 = int(input())

    Ret = Multiplication(Value1,Value2)

    print("Multiplication of number is:",Ret)


if __name__ == "__main__":
    main()