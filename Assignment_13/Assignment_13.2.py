############################################################################
#
#      Write a program that accepts radius of a circle
#      and prints the area of the circle.
#
#############################################################################

def AreaOfCircle(r):
    
    pi = 3.14
    Area = pi * r * r

    print("Area of circle is :",Area)
     

def main():
    
    No1 = 0

    print("Enter the radius of a circle number:")
    No1 = int(input())

    AreaOfCircle(No1)

if __name__ == "__main__":
    main()
