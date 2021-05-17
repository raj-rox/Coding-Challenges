#Solved it in n^2 time on 1st attempt. nlogn was challenging. Just see if can remember the nlogn soln
#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    # arr=list(set(arr1))
    arr.sort()
    mad=abs(arr[0]-arr[1])
    for i in range(1,len(arr)):
        if mad>abs(arr[i]-arr[i-1]):
            mad=abs(arr[i]-arr[i-1])
    return mad
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
