##############################################################################
#
# Write a program which accepts N numbers from user
# and stores them into a list.
# Return the addition of all elements from that list.
#
##############################################################################


def Addition(No):

    Sum = 0
    
    for i in No:
        Sum = Sum + i

    return Sum

def main():

    Value = 0
    Result = list()
    Ret = 0

    print("Enter the value:")
    Value = int(input())

    print("Enter the elements: ")
    for i in range(Value):
            Value = int(input())
            Result.append(Value)
    
    Ret = Addition(Result)
    print("Addition of elements is:",Ret)

if __name__ == "__main__":
    main()