https://www.hackerrank.com/challenges/staircase/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    hashes=1
    spaces=n-1
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,i):
            print("#",end="")
        print("")
if __name__ == '__main__':
    n = int(input())

    staircase(n)
