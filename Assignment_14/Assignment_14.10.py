###################################################################################
#
#    Accept three numbers and return the largest number.
#
#####################################################################################

Largest = lambda No1 ,No2 ,No3 : No1 if (No1 > No2 and No1 > No3) else No2 if (No2 > No1 and No2 > No3) else No3 


def main():

    Value1 = 0
    Value2 = 0
    Value3 = 0
    Ret = 0

    print("Enter the First number:")
    Value1 = int(input())

    print("Enter the  Second number:")
    Value2 = int(input())

    print("Enter the Third number:")
    Value3 = int(input())

    Ret = Largest(Value1,Value2,Value3)

    print("Largest number is:",Ret)


if __name__ == "__main__":
    main()