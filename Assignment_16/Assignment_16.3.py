
##############################################################################
#
# Write a program which contains one function named as Add()
# which accepts two numbers from user
# and returns the addition of those two numbers.
#
##############################################################################



def Add(No1,No2):
    Ans = 0

    Ans = No1 + No2
    return Ans

def main():

    Value1 = 0
    Value2 = 0

    Ret = 0

    print("Enter the First number")
    Value1 = int(input())

    print("Enter the Second number")
    Value2 = int(input())

    Ret = Add(Value1,Value2)

    print("Addition is :",Ret)

if __name__ == "__main__":
    main()