############################################################################
#
#      Write a program that accepts two numbers
#      and prints addition, subtraction,
#      multiplication and division of those numbers.
#
#############################################################################

def DisplayOperation(Value1,Value2):
     

    Ans1 = Value1 + Value2
    Ans2 = Value1 - Value2
    Ans3 = Value1 * Value2
    Ans4 = Value1 / Value2

    return Ans1 ,Ans2 ,Ans3 , Ans4


def main():
    
    No1 = 0
    No2 = 0

    print("Enter the First number:")
    No1 = int(input())

    print("Enter the Second number:")
    No2 = int(input())

    Add,Sub,Mul,Div = DisplayOperation(No1,No2)

    print("Addition is:",Add)
    print("Substraction is:",Sub)
    print("Multiplication is:",Mul)
    print("Division is:",Div)

if __name__ == "__main__":
    main()
