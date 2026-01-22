###################################################################################
#
#     Accept a list of numbers and return the product of all elements
#     using reduce().
#
#####################################################################################


Product = lambda A, B: A * B 

def reduceX(Task,Elements):

    prod = 1
    for no in Elements:
        prod = Task(prod,no)


    return prod 
    
def main():

    Data = [12,15,34,5,25,9,30,35,40]
    print("Actual Data before filter:",Data)

    RData = reduceX(Product,Data)
    print("Data after reduce:",RData)


if __name__ == "__main__":
    main()