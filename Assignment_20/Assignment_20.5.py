##############################################################################
#
# Design a Python application that creates two threads named
# Thread1 and Thread2.
#
# Thread1 should display numbers from 1 to 50.
#
# Thread2 should display numbers from 50 to 1 in reverse order.
#
# Ensure that:
#   - Thread2 starts execution only after Thread1 has completed.
#   - Appropriate thread synchronization is used.
#
##############################################################################


import threading

def Display(No):

    for i in range(1,No+1,1):
        
        print(i)

def ReverseDisplay(No):

    for i in range(No+1,0,-1):
        
        print(i)


def main():

    Value = 50

    t1 = threading.Thread(target=Display, args=(Value,))
    t2 = threading.Thread(target=ReverseDisplay, args=(Value,))
     
    t1.start()
    t1.join()
  
    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
