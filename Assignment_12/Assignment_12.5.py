############################################################################
#
#       Write a program that accepts one number
#      and prints that many numbers in reverse order.
#      Input  : 5
#      Output : 5 4 3 2 1
#
#############################################################################

def DisplayNoRev(Value):
     
    for i in range(Value,0,-1):
            print(i,end=" ")
     

def main():
    
    No = 0

    print("Enter the number:")
    No = int(input())

    DisplayNoRev(No)

if __name__ == "__main__":
    main()

