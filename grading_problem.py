https://www.hackerrank.com/challenges/grading/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    finalgrade=[]
    for grade in grades:
        if grade<38:
            finalgrade.append(grade)
            continue
        else:
            if (int((grade/5+1))*5-grade)<3:
                finalgrade.append(int((grade/5+1))*5)
            else:
                finalgrade.append(grade)
    return finalgrade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
