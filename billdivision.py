#https://www.hackerrank.com/challenges/bon-appetit/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    index=k
    sum=0
    for i in range(0,len(bill)):
        if i==index:
            continue
        sum+=bill[i]
    # print("sum is", sum)
    if sum/2==b:
        print("Bon Appetit")
    else:
        print(int(b-sum/2))
        
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
