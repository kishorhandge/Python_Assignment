############################################################################
#
#      Write a program that accepts length and width of a rectangle
#      and prints the area of the rectangle.
#
#############################################################################

def AreaOfRectangle(length,width):
     
    Area = length * width

    print("Area of reactnangle is :",Area)
     

def main():
    
    No1 = 0
    No2 = 0

    print("Enter the length number:")
    No1 = int(input())

    print("Enter the width number:")
    No2 = int(input())

    AreaOfRectangle(No1,No2)

if __name__ == "__main__":
    main()
