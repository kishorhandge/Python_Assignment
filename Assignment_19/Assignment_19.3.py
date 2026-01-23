##############################################################################
#
# Write a program which contains filter(), map() and reduce().
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
#
# Filter should filter out all such numbers
# which are greater than or equal to 70 and less than or equal to 90.
#
# Map function will increase each number by 10.
# Reduce will return product of all that numbers.
#
# Input List        : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter : [76, 89, 86, 90, 70]
# List after map    : [86, 99, 96, 100, 80]
# Output of reduce  : 653875200
#
##############################################################################

from functools import reduce

Sort = lambda No : (No >= 70 and No<= 90)

Increment = lambda No : No + 10

Product = lambda A,B: A * B  
    
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

    FData = list(filter(Sort,Data))
    print("Data after filter:",FData)

    MData = list(map(Increment,FData))
    print("Data after map:",MData)

    RData = (reduce(Product,MData))
    print("Data after reduce:",RData)



if __name__ == "__main__":
    main()