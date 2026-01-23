##############################################################################
#
# Write a program which contains filter(), map() and reduce().
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
#
# Filter should filter out all such numbers which are even.
# Map function will calculate its square.
# Reduce will return addition of all that numbers.
#
# Input List        : [5, 2, 3, 4, 2, 1, 2, 8, 10]
# List after filter : [2, 4, 2, 2, 8, 10]
# List after map    : [4, 16, 4, 4, 64, 100]
# Output of reduce  : 192
#
##############################################################################


from functools import reduce

CheckEven = lambda No : (No%2 == 0)

Square = lambda No : No * No

Add = lambda A,B: A + B  
    
def main():

    No = 0
    Ret = 0
    
    print("Enter the number of elements:")
    No = int(input())

    Data = list()

    print("Enter the elements number:")
     
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    print("Actual Data before operation:",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after filter:",FData)

    MData = list(map(Square,FData))
    print("Data after map:",MData)

    RData = (reduce(Add,MData))
    print("Data after reduce:",RData)



if __name__ == "__main__":
    main()