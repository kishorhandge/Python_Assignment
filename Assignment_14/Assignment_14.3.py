###################################################################################
#
#    Accept two numbers and return the maximum number.
#
#####################################################################################

Maximum = lambda No1 ,No2  : No1 if (No1 > No2) else (No2)


def main():

    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter the First number:")
    Value1 = int(input())

    print("Enter the  Second number:")
    Value2 = int(input())

    Ret = Maximum(Value1,Value2)

    print("Maximum number is:",Ret)

if __name__ == "__main__":
   main()

