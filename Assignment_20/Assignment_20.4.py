##############################################################################
#
# Design a Python application that creates three threads named
# Small, Capital, and Digits.
#
# All threads should accept a string as input.
#
# The Small thread should count and display
# the number of lowercase characters.
#
# The Capital thread should count and display
# the number of uppercase characters.
#
# The Digits thread should count and display
# the number of numeric digits.
#
# Each thread must also display:
#   - Thread ID
#   - Thread Name
#
##############################################################################

import threading

def LowerCase(Str):
    Count = 0

    for ch in Str:
        if(ch >= 'a' and ch <= 'z'):
            Count = Count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lower Case Letter Count:", Count)
    print("----------------------------------")

def UpperCase(Str):
    Count = 0

    for ch in Str:
        if(ch >= 'A' and ch <= 'Z'):
            Count = Count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Upper Case Letter Count:", Count)
    print("----------------------------------")

def Digits(Str):
    Count = 0

    for ch in Str:
        if(ch >= '0' and ch <= '9'):
            Count = Count + 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digit Count:", Count)
    print("----------------------------------")

def main():

    Value = "Kishor Handge 1234"

    t1 = threading.Thread(target=LowerCase, args=(Value,))
    t2 = threading.Thread(target=UpperCase, args=(Value,))
    t3 = threading.Thread(target=Digits, args=(Value,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
