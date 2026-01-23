
##############################################################################
#
# Write a program which accepts one number from user
# and returns its factorial.
#
##############################################################################


def DisplayFactorial(No):
     
    Fact = 1
    for i in range(1,No + 1,1):
        Fact = Fact * i
    
    print("Factorial is :",Fact)
         
            
def main():

    Value = 0

    print("Enter the number")
    Value = int(input())

    DisplayFactorial(Value)

if __name__ == "__main__":
    main()