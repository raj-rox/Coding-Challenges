https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min=arr[0]+arr[1]+arr[2]+arr[3]
    max=arr[0]+arr[1]+arr[2]+arr[3]
    for i in range(len(arr)):
        sum=arr[i%len(arr)]+arr[(i+1)%len(arr)]+arr[(i+2)%len(arr)]+arr[(i+3)%len(arr)]
        if sum<min:
            min=sum
        if sum>max:
            max=sum
    print(min,end=" ")
    print(max)
    return 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
