############################################################################
#
#      Write a program that accepts one number
#      and prints that many numbers starting from 1.
#      Input  : 5
#      Output : 1 2 3 4 5
#
#############################################################################

def DisplayStarting(Value):
     
    for i in range(1,Value + 1):
            print(i,end=" ")
     

def main():
    
    No = 0

    print("Enter the number:")
    No = int(input())

    DisplayStarting(No)

if __name__ == "__main__":
    main()

