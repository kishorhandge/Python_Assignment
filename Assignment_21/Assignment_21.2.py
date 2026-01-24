##############################################################################
#
# Write a Python program which creates two threads.
#
# Thread 1 should calculate and display the maximum element from a list.
#
# Thread 2 should calculate and display the minimum element from the same list.
#
# The list should be accepted from the user.
#
##############################################################################



import threading

def Maximum(Arr):

    print("Maximum number are:")

    Largest = Arr[0]
    
    for i in range(len(Arr)):
        if(Arr[i] > Largest):
            Largest = Arr[i]
        
    print(Largest)
    
def Minimum(Arr):

    print("Minimum number are:")

    Small = Arr[0]
    
    for i in range(len(Arr)):
        if(Arr[i] < Small):
            Small = Arr[i]
        
    print(Small)

def main():

    Data = [10,11,12,13,14,15,16,17]

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))
     
    t1.start()
    t1.join()
  
    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
