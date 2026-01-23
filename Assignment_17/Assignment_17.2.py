
##############################################################################
#
# Write a program which accepts one number from user
# and displays the following pattern.
#
# Input  : 5
# Output :
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
#
##############################################################################



def Display(No):
     
    for i in range(No):
        for j in range(No):
            print("*",end=" ")
        print()
            
def main():

    Value = 0

    print("Enter the number")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()