###################################################################################
#
#      Accept a list of numbers and return a list of squares of each number
#     using map().
#
#####################################################################################


Square = lambda No : (No * No)

def mapX(Task,Elements):

    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def main():

    Data = [10,11,12,20]
    print("Actual Data before map:",Data)

    MData = list(mapX(Square,Data))
    print("Data after map:",MData)


if __name__ == "__main__":
    main()