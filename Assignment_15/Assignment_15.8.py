###################################################################################
#
#     Accept a list of numbers and return a list of numbers divisible
#     by both 3 and 5 using filter().
#
#####################################################################################


Divisible = lambda No1 :  (No1%3 == 0 and No1%5 == 0)

def filterX(Task,Elements):

    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)

    return Result
    
def main():

    Data = [12,15,34,5,25,9,30,35,40]
    print("Actual Data before filter:",Data)

    FData = list(filterX(Divisible,Data))
    print("Data after filter:",FData)


if __name__ == "__main__":
    main()