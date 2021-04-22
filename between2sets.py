#https://www.hackerrank.com/challenges/between-two-sets/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    max_a=a[0]
    min_b=b[0]
    ans=0
    for i in a:
        if i>max_a:
            max_a=i
    for i in b:
        if i<min_b:
            min_b=i
    for element in range(max_a,min_b+1):
        flag1=1
        flag2=1
        for j in range(0,len(a)):
            if element%a[j]!=0:
                flag1=0
                break
        for k in range(0,len(b)):
            if b[k]%element!=0:
                flag2=0
                break
        # print("j is",j)
        # print("k is",k)
        if flag1==1 and flag2==1:
            ans+=1
            # print("answer is"+str(ans))
            # print("element is"+str(element))
    return ans    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
