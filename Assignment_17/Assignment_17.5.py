
##############################################################################
#
# Write a program which accepts one number from user
# and checks whether the number is prime or not.
#
##############################################################################

def Prime(No):
     
    Count = 0

    for i in range(2,No):
        if(No%i == 0):
           return False
             
    
    return True
         
def main():

    Value = 0
    Ret = 0

    print("Enter the number")
    Value = int(input())

    Ret = Prime(Value)
    if(Ret == True):
        print("It is a Prime Number:")

    else:
        print("It is not a Prime Number")

if __name__ == "__main__":
    main()