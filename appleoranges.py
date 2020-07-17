https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #apples & oranges are the lists
    #If a+apples[i]<s,t>
    #If b+oranges[i]<s,t>
    counta =0
    counto=0
    for i in apples:
        if a+i>=s and t>=a+i:
            counta+=1
    for i in oranges:
        if b+i>=s and t>=b+i:
            counto+=1
    print(counta)
    print(counto)
    return

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
