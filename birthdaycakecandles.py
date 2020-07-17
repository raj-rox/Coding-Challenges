https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
#Count_max.
    count_max=0
    max=ar[0]
    for i in ar:
        if i>max:
            max=i
            count_max=1
        elif i==max:
            count_max+=1
    return count_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
