##############################################################################
#
# Design a Python application that creates two threads named
# EvenList and OddList.
#
# Both threads should accept a list of integers as input.
#
# The EvenList thread should:
#   - Extract all even elements from the list.
#   - Calculate and display their sum.
#
# The OddList thread should:
#   - Extract all odd elements from the list.
#   - Calculate and display their sum.
#
# Threads should run concurrently.
#
##############################################################################


import threading

def Even(No):
    Sum = 0
    print("Even No are:")
    for i in No:
        if No % 2 == 0 :
            print(i)
            Sum = Sum + i
    print("Sum of even No:", Sum)

def Odd(No):
    Sum = 0
    print("Odd No are:")
    for i in No:
        if No % 2 != 0:
            print(i)
            Sum = Sum + i
    print("Sum of odd No:", Sum)

def main():

    Value = [10, 21, 30, 41, 50, 63, 72, 85]

    t1 = threading.Thread(target=Even, args=(Value,))
    t2 = threading.Thread(target=Odd, args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
