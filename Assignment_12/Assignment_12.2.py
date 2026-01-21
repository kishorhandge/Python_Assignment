############################################################################
#
#      Write a program that accepts one number
#      and prints all factors of that number.
#      Input  : 12
#      Output : 1 2 3 4 6 12
#
#############################################################################

def DisplayFactor(Value):
     
    for i in range(1,Value + 1):
        if(Value % i == 0):
            print(i,end=" ")
     

def main():
    
    No = 0

    print("Enter the number:")
    No = int(input())

    DisplayFactor(No)

if __name__ == "__main__":
    main()
