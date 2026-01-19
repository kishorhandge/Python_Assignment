############################################################################
#
#       Write a program that accepts one number
#      and checks whether it is palindrome or not.
#      Input  : 121
#      Output : Palindrome
#
#############################################################################

def CheckPalindrome(Value):
     
    Digit = 0
    temp = Value
    Rev = 0

    while(Value != 0):
        Digit = Value % 10
        Rev = (Rev *10) + Digit
        Value = Value // 10

    if(temp == Rev):
        return True
    else:
        return False
     

def main():

    bRet = False
    print("Enter the number:")
    No = int(input())

    bRet = CheckPalindrome(No)

    if(bRet == True):
        print("It is Palindrome:")

    else:
         print("It Not a Palindrome:")

if __name__ == "__main__":
    main()
