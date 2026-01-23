##############################################################################
#
# Write a program which accepts N numbers from user
# and stores them into a list.
# Accept one more number from user
# and return the frequency of that number from the list.
#
##############################################################################


def Frequency(Arr,No):

    Freq = 0
    
    for i in Arr:
        if(i == No):
            Freq = Freq + 1

    return Freq

def main():

    Value1 = 0
    Value2 = 0
    Result = list()
    Ret = 0

    print("Enter the value:")
    Value = int(input())

    print("Enter the elements: ")
    for i in range(Value):
            Value = int(input())
            Result.append(Value)

    print("Enter the number:")
    Value2 = int(input())
    
    Ret = Frequency(Result,Value2)
    print("Frequecy of number is:",Ret)

if __name__ == "__main__":
    main()