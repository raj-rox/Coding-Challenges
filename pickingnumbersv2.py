#!/bin/python3
#https://www.hackerrank.com/challenges/picking-numbers/problem
import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    count=0
    count_max=1
    x=set(a)
    for i in x:
        b=a.count(i)
        c=a.count(i-1)
        count=c+b
        if count>count_max:
            count_max=count
    return count_max
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
