#https://www.hackerrank.com/challenges/plus-minus/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_positive, count_zero,count_negative=0,0,0
    count_total=len(arr)
    for i in arr:
        if i>0:
            count_positive+=1
        elif i<0:
            count_negative+=1
        else:
            count_zero+=1
    print(count_positive/count_total)
    print(count_negative/count_total)
    print(count_zero/count_total)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
