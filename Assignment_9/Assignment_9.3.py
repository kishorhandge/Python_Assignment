#######################################################################
#      Write a program that accepts one number
#       and prints the square of that number.
#       Input  : 5
#       Output : 25
#
######################################################################


def  Square(Value):
    
    sqr = Value * Value

    print("Square is:",sqr)
     

def main():

    No = 0
 
    print("Enter the number")
    No = int(input())

    Square(No)
    

if __name__ == "__main__":
    main()

