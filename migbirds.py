#https://www.hackerrank.com/challenges/migratory-birds/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    unique_arr=set(arr)
    unique_arr=list(unique_arr)
    maxcount=1
    for i in range(0,len(unique_arr)):
        count=0
        for j in range(0,len(arr)):
            if unique_arr[i]==arr[j]:
                count+=1
        if count>maxcount:
            maxcount=count
            maxelement=unique_arr[i]
    return maxelement

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
