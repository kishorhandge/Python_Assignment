
##############################################################################
#
# Write a program which accepts name from user
# and displays the length of its name.
#
##############################################################################


def Display(No):
    
    print("Length of name is: ")
    print(len(No))
            
def main():

    Value = 0

    print("Enter the name")
    Value = (input())

    Display(Value)

if __name__ == "__main__":
    main()