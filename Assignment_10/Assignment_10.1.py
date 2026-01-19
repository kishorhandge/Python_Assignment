############################################################################
#
#       Write a program that accepts one number
#       and prints the multiplication table of that number.
#       Input  : 4
#       Output : 4 8 12 16 20 24 28 32 36 40
#
#############################################################################
 

def  Table(Value):
    
    for i in range(4,41,4):
        print(i)
     

def main():

    No = 0
 
    print("Enter the number")
    No = int(input())

    Table(No)


if __name__ == "__main__":
    main()

