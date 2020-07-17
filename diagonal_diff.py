https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    pri_diagonal,sec_diagonal=0,0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i==j:
                pri_diagonal+=arr[i][j]
            if(i+j==len(arr)-1):
                sec_diagonal+=arr[i][j]
    return abs(pri_diagonal-sec_diagonal)
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
