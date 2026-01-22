
##############################################################################
#
# Write a program which accepts a number from user
# and prints that number of "*" on screen.
#
##############################################################################


def Display(No):
     
    for i in range(1,No +1,1):
        print("*",end=" ")
            
def main():

    Value = 0

    print("Enter the number")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()