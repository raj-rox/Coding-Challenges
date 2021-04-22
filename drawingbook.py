#https://www.hackerrank.com/challenges/drawing-book/problem
#!/bin/python3

import os
import sys
import math
#
# Complete the pageCount function below.
#
def pageCount(n, p):
    return(min(p//2, n//2 - p//2))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

    
#     def pageCount(n, p):
#     #
#     # Write your code here.
#     #1? n==p?
#     if p-1>=n-p:
#     	return (n-p)/2
#     if n-p>p-1:
#     	return ceil(p-1)/2

# result = pageCount(n, p)
# print(result)
