##############################################################################
#
# Write a Python program where multiple threads update a shared variable.
#
# Use a Lock to avoid race conditions.
#
# Each thread should increment the shared counter multiple times.
#
# Display the final value of the counter after all threads complete execution.
#
##############################################################################


import threading

Counter = 0
lobj = threading.Lock()

def Increment():

    global Counter
    
    for i in range(1000):
        with lobj:
           Counter+=1

def main():

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)
    t3 = threading.Thread(target=Increment)
     
    t1.start()
    t2.start()
    t3.start()
    
    t2.join()
    t1.join()
    t3.join()

    print("Final Value of couner:",Counter)

if __name__ == "__main__":
    main()
