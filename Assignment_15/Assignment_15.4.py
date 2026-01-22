###################################################################################
#
#      Accept a list of numbers and return the addition of all elements
#     using reduce().
#
#####################################################################################


Add = lambda No1, No2 :  No1 + No2

def reduceX(Task,Elements):

    sum = 0

    for no in Elements:
        sum = Task(sum,no)

    return sum

def main():

    Data = [10,11,12,20]
    print("Actual Data before filter:",Data)

    RData = reduceX(Add,Data)
    print("Data after reduce:",RData)


if __name__ == "__main__":
    main()