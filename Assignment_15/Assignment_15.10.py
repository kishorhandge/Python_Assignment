###################################################################################
#
#     Accept a list of numbers and return the count of even numbers
#     using filter().
#
#####################################################################################


EvenCount = lambda No : (No%2 == 0)

def filterX(Task,Elements):

    Result = list()
    Count = 0

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Count = Count + 1

    return Count
    
def main():

    Data = [12,15,34,5,25,9,30,35,40]
    print("Actual Data before filter:",Data)

    FData = filterX(EvenCount,Data)
    print("Data after filter:",FData)


if __name__ == "__main__":
    main()