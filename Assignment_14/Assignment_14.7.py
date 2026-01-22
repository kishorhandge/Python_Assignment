###################################################################################
#
#     Accept one number and return True if the number is divisible by 5.
#
#####################################################################################

CheckDiv = lambda No : True  if (No % 5 == 0) else False

def main():

    Value = 0
    Ret = False

    print("Enter the number:")
    Value = int(input())

    Ret = CheckDiv(Value)

    if(Ret == True):
        print("Number is Divisible by 5")

    else:
        print("Number is Divisible by 5 ")


if __name__ == "__main__":
    main()