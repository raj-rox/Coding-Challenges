#Q: Day 7, 30 days of code, hackerrank 
#!/bin/python3

import math
import os
import random
import re
import sys


def reversal(a):
    n=len(a)
    for i in range(int(n/2)):
        temp=a[i]
        a[i]=a[n-i-1]
        a[n-i-1]=temp
    print(*a, sep = " ")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reversal(arr)
