###################################################################################
#
#     Accept a list of strings and return a list of strings having
#     length greater than 5 using filter().
#
#####################################################################################


Length = lambda str : len(str) > 5

def filterX(Task,Elements):

    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)

    return Result
    
def main():

    Data = ["iam","is","not","normal","always"]
    print("Actual Data before filter:",Data)

    FData = list(filterX(Length,Data))
    print("Data after filter:",FData)


if __name__ == "__main__":
    main()