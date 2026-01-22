
##############################################################################
#
# Write a program which accepts a number from user
# and checks whether the number is positive, negative or zero.
#
##############################################################################


def Check(No):
     
    if(No < 0):
        print("Negative Number.")

    elif(No > 0):
        print("Positive Number.")
    else:
        print("Number is Zero.")
        

def main():

    Value = 0

    print("Enter the number")
    Value = int(input())

    Check(Value)

if __name__ == "__main__":
    main()