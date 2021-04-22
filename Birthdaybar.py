#https://www.hackerrank.com/challenges/the-birthday-bar/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count=0
    window=[]
    if len(s)<m:
        return count
    if len(s)==1 and m==1:
        if s[0]==d:
            count+=1
            return count
        else:
            return count
    if len(s)>1 and len(s)>m:    
        for i in range(0,len(s)-m+1):
            sumwindow=0
            for j in range(0,m):
                sumwindow+=s[i+j]
            print("i is"+str(i))
            print("sumwindow is"+str(sumwindow))
            if sumwindow==d:
                count+=1
            window=[]
        return count
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
