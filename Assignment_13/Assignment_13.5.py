############################################################################
#
#      Write a program that accepts marks
#      and displays the grade according to the following conditions:
#
#      >= 75  : Distinction
#      >= 60  : First Class
#      >= 50  : Second Class
#      <  50  : Fail
#
#############################################################################

def DisplayGrade(Value):
    
    if(Value >= 75):
        print("Destination:")
    elif(Value >= 60):
        print("First Class:")
    elif(Value >= 50):
        print("Second Class:")
    elif(Value < 50):
        print("Fail")
    else:
        print("No Attempted")


def main():
    
    No1 = 0

    print("Enter the marks:")
    No1 = int(input())

    DisplayGrade(No1)

if __name__ == "__main__":
    main()
