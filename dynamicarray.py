
#https://www.hackerrank.com/challenges/dynamic-array/problem
# def dynamicArray(n, queries):

#     # initialize a variable no of arrays..done
# 	rows = n
# 	arr = []
# 	ans=[]
# 	for i in range(0,n):
# 		arr.append([])
# 	lastAnswer=0
# 	for i in range(0,len(queries)):
# 		if queries[i][0]==1:
# 			idx=((queries[i][1]^lastAnswer)%n)
#     		#how to append an element to a nested 2d list..done
# 			arr[idx].append(queries[i][2])
# 			# print("arr is"+str(arr))
# 		if queries[i][0]==2:
# 			idx=((queries[i][1]^lastAnswer)%n)
# 			# print("idx is"+str(idx))
# 			lastAnswer=arr[idx][queries[i][2]%len(arr[idx])]
# 			# print(lastAnswer)
# 			ans.append(lastAnswer)
#             # print(lastAnswer)

# queries=[[1, 0, 5],[1, 1, 7],[1, 0, 3],[2, 1, 0],[2, 1, 1]]
# n=2
# result = dynamicArray(n, queries)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    ans=[]
    # initialize a variable no of arrays..done
    rows = n
    arr = []
    for i in range(0,n):
        arr.append([])
    lastAnswer=0
    for i in range(0,len(queries)):
        if queries[i][0]==1:
            idx=((queries[i][1]^lastAnswer)%n)
            #how to append an element to a nested 2d list..done
            arr[idx].append(queries[i][2])
            # print("arr is"+str(arr))
        if queries[i][0]==2:
            idx=((queries[i][1]^lastAnswer)%n)
            # print("idx is"+str(idx))
            lastAnswer=arr[idx][queries[i][2]%len(arr[idx])]
            ans.append(lastAnswer)
            # print(lastAnswer)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

