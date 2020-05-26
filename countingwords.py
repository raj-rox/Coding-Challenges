# Python 3 program to find the number of words
# of X vowels and Y consonants can be
# formed from M vowels and N consonants

# Function to returns factorial of n
def fact(n):
    res = 1
    for i in range(2, n + 1, 1):
        res = res * i
    return res

# Function to find nCr
def nCr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

# Function to find the number of words
# of X vowels and Y consonants can be
# formed from M vowels and N consonants
def NumberOfWays(X, Y, M, N):
    return fact(X + Y) * nCr(M, X) * nCr(N, Y)

# Driver code
if __name__ == '__main__':
    X = 1
    Y = 1
    M = 5
    N = 21
    #If n is given. and x>1 & y=n-1
    n=2
    while(X<=n):
        Y=n-X
        
        X+=1
    # Function call
    print(NumberOfWays(X, Y, M, N))
