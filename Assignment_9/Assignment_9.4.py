#######################################################################
#       Write a program that accepts one number
#       and prints the cube of that number.
#
######################################################################


def  Cube(Value):
    
    cb = Value * Value * Value

    print("Cube is:",cb)
     

def main():

    No = 0
 
    print("Enter the number")
    No = int(input())

    Cube(No)
    

if __name__ == "__main__":
    main()

