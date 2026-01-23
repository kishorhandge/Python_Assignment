##############################################################################
#
# Write a program which accepts N numbers from user
# and stores them into a list.
# Return the minimum number from that list.
#
##############################################################################


def Minimum(Arr):

    Mini = Arr[0]
    
    for i in Arr:
        if(i < Mini):
            Mini = i

    return Mini

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
    
    Ret = Minimum(Result)
    print("Minimum number is:",Ret)

if __name__ == "__main__":
    main()