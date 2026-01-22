###################################################################################
#
#    Accept one number and return True if the number is odd,
#     otherwise return False.
#
#####################################################################################

OddCheck = lambda No : True  if (No % 2 == 0) else False

def main():

    Value = 0
    Ret = False

    print("Enter the number:")
    Value = int(input())

    Ret = OddCheck(Value)

    if(Ret == True):
        print("Number is Even Number")

    else:
        print("Number is Odd Number")


if __name__ == "__main__":
    main()