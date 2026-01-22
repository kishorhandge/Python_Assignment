
##############################################################################
#
# Write a program which contains one function named as ChkNum()
# which accepts one parameter as number.
# If number is even then display "Even Number",
# otherwise display "Odd Number" on console.
#
##############################################################################


def ChkNum(No):

    if(No%2 == 0):
        return True
    else:
        return False

def main():

    Value = 0
    Ret = False

    print("Enter the number")
    Value = int(input())

    Ret = ChkNum(Value)

    if(Ret == True):
        print("Even Number")

    else:
        print("Odd Number")

if __name__ == "__main__":
    main()