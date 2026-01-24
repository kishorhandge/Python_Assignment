##############################################################################
#
# Write a Python program which creates two threads named Prime and NonPrime.
#
# Both threads should accept a list of integers.
#
# Prime thread should display all prime numbers from the list.
#
# NonPrime thread should display all non-prime numbers from the list.
#
##############################################################################


import threading

def ChkPrime(No):

    for i in range(2,No):
        if(No%i == 0):
            return False
        else:
            return True

def Prime(Arr):

    print("Prime number are:")

    for i in Arr:
        if(ChkPrime(i)):

            print(i,end=" ")

    print()

def NonPrime(Arr):

    print("Non-Prime number are:")

    for i in Arr:
        if not(ChkPrime(i)):

            print(i,end=" ")

    print()

def main():

    Data = [10,11,12,13,14,15,16,17]

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args=(Data,))
     
    t1.start()
    t1.join()
  
    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
