
##############################################################################
#
# Write a program which accepts one number from user
# and displays the following pattern.
#
# Input  : 5
# Output :
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5
#
##############################################################################



def Display(No):

    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,end=" ")
        print()
    
def main():

    Value = 0
    Ret = 0

    print("Enter the number")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()