##############################################################################
#
# Write a Python program which creates two threads.
#
# Thread 1 should compute the sum of elements from a list.
#
# Thread 2 should compute the product of elements from the same list.
#
# Return the results to the main thread and display them.
#
##############################################################################


import threading

SumResult = 0
ProductResult = 1

def Sum(Arr):

    global SumResult 
    
    for i in (Arr):
        SumResult = SumResult + i

        
    return SumResult
    
def Product(Arr):
    
    global ProductResult 

    for i in (Arr):
        ProductResult = ProductResult * i

    
    return ProductResult

def main():

    Data = [10,20,30,40]

    t1 = threading.Thread(target=Sum, args=(Data,))
    t2 = threading.Thread(target=Product, args=(Data,))
     
    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("Sum of elements is:", SumResult)
    print("Product of elements is:", ProductResult)
    print("Exit from main")

if __name__ == "__main__":
    main()
