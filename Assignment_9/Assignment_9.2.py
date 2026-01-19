#######################################################################
#       Write a program that contains one function ChkGreater()
#       which accepts two numbers and prints the greater number.
#       Input  : 10 20
#       Output : 20 is greater
#
######################################################################

def ChkGreater(Value1 ,Value2):
    
    if(Value1 > Value2):
        print("No1 is greater.")

    else:
       print("No2 is greater.") 

def main():

    No1 = 0
    No2 = 0

    print("Enter the first number")
    No1 = int(input())

    print("Enter the first number")
    No2 = int(input())

    ChkGreater(No1 , No2)
    

if __name__ == "__main__":
    main()

