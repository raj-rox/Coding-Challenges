#Mar marke samja. N2 implementation was cool. Hashmap was a bit fucking annoying.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    parlor=dict()
    for i in range(len(arr)):
        if arr[i] not in parlor:
            parlor[m-arr[i]]=i+1
        else:
            # x=sorted(i+1,parlor[arr[i]])
            return sorted([i+1, parlor[arr[i]]])
            # def icecreamParlor(m, arr):
#     test = dict()
#     for i in range(len(arr)):
#         if arr[i] not in test: 
#             test[m-arr[i]] = i+1 #dollar match amount is key, 1based index is value
#         else:
#             return sorted([i+1, test[arr[i]]])    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
