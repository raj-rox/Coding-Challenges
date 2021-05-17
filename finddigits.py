#Hogaya 1st attempt mai. DONE
#https://www.hackerrank.com/challenges/find-digits/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    count=0
    copy=n
    while(n!=0):
        if n%10!=0 and copy%(n%10)==0:
            count+=1
        n=int(n/10)
    return count 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
