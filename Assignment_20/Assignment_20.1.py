##############################################################################
#
# Design a Python application that creates two separate threads
# named Even and Odd.
#
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
#
##############################################################################

import threading
import time

def Even(No):
    for i in range(2, No + 1, 2):
        print(i)
        time.sleep(0.04)

def Odd(No):
    for i in range(1, No + 1, 2):
        print(i)
        time.sleep(0.01)

def main():

    t1 = threading.Thread(target=Even, args=(20,))   
    t2 = threading.Thread(target=Odd, args=(19,))    

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
