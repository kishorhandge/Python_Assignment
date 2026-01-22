
##############################################################################
#
# Write a program which displays numbers from 10 to 1 on screen.
#
##############################################################################

def DisplayRev(No):
     
    for i in range(No,0,-1):
        print(i,end=" ")

def main():

    DisplayRev(10)

if __name__ == "__main__":
    main()