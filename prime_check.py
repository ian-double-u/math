def prime_check(m): # returns True if n is prime, False otherwise
    n = m**2
    
    A = [True]*n
    for i in range(2,int(n**(0.5))+1): 
        if A[i] == True:
            j = i**2
            while j < n:
                A[j] = False
                j += i                  
    A_ = [i for i in range(len(A)) if A[i] == True][2:]
    
    if m in A_: return True
    else: return False