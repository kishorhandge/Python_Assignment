
##############################################################################
#
# Write a program which displays the first 10 even numbers on screen.
#
##############################################################################


def Display(No):
     
    for i in range(2,No +1,2):
        if(No%2 == 0):
            print(i,end=" ")
            
def main():

    Value = 0

    print("Enter the number")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()