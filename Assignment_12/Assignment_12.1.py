############################################################################
#
#       Write a program that accepts one character
#      and checks whether it is a vowel or consonant.
#      Input  : a
#      Output : Vowel
#
#############################################################################

def CheckVowel(Value):
     
    if(Value == 'a' or Value == 'e' or Value == 'i' or Value == 'o' or Value == 'u'
       or Value == 'A' or Value == 'E' or Value == 'I' or Value == 'O' or Value == 'U'):
        print("It is Vowel:")
    else:
        print("It Is Not Vowel:")
     

def main():

    print("Enter the character:")
    ch = input()

    CheckVowel(ch)

if __name__ == "__main__":
    main()
