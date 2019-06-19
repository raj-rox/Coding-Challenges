This is the solution to the challenge: https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
CODE:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s=list(s)
    CountOfaInS=0
    for i in range(0,len(s)):
        if s[i]=="a":
            CountOfaInS+=1
    count=0
    l=len(s)
    q=n//l
    r=n%l
    i=0
    remainder=0
    while(r!=0):
        if(s[i]=='a'):
            remainder+=1
        r=r-1
        i=i+1
    return (CountOfaInS*q+remainder)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
