###################################################################################
#
#     Accept a list of numbers and return the minimum element using
#     reduce().
#
#####################################################################################


Minimum = lambda No1, No2 :  No1 if (No1 < No2) else No2

def reduceX(Task,Elements):

    Result = Elements[0]

    for no in Elements[1:]:
        Result = Task(Result,no)

    return Result

def main():

    Data = [10,11,12,20]
    print("Actual Data before filter:",Data)

    RData = reduceX(Minimum,Data)
    print("Data after reduce:",RData)


if __name__ == "__main__":
    main()