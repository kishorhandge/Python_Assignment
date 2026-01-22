###################################################################################
#
#      Accept a list of numbers and return a list of odd numbers using
#     filter().
#
#####################################################################################


Odd = lambda No : (No%2 == 1)

def filterX(Task,Elements):

    Result = list()

    for no in Elements:
        Ret = Task(no)
         
        if(Ret == True):
           Result.append(no)

    return Result

def main():

    Data = [10,11,12,20]
    print("Actual Data before filter:",Data)

    MData = list(filterX(Odd,Data))
    print("Data after filer:",MData)


if __name__ == "__main__":
    main()