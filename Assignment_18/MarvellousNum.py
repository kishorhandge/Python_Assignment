def ChkPrime(Arr):
    
    for i in range(2,Arr):
        if(Arr % i == 0):
            return False
        else:
            return True
    