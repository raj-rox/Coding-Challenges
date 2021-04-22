#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=false

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    ans=""
    if (s[len(s)-2]=="P") and ((int(s[0]+s[1]))!=12):
        n1=10*int(s[0])+int(s[1])
        n1+=12
        n1=n1%24
        ans+=str(n1)
        ans+=s[2:-2]
    if (s[len(s)-2]=="P") and ((int(s[0]+s[1]))==12):
        ans=s[0:-2]    
    if (s[len(s)-2]=="A") and ((int(s[0]+s[1]))!=12):
        n1=10*int(s[0])+int(s[1])
        n1=n1%12
        if n1==10 or n1==11:
            ans=ans+str(n1)
        else:
            ans=ans+"0"+str(n1)
        ans+=s[2:-2]
    if (s[len(s)-2]=="A") and ((int(s[0]+s[1]))==12):
        n1="0"
        ans+=str(n1)
        ans+=str(n1)
        ans+=s[2:-2]
    return ans
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
