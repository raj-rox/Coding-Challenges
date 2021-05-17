#Easy qn..but had to see the soln. Diff implementing Qn language
#https://www.hackerrank.com/challenges/strange-advertising/problem
import math


def  viralAdvertising(n):
        cumulative=0
        liked=0
        shared=5
        for i in range(1, n+1):
            liked=math.floor(shared/2)
            shared=3*liked    
            cumulative+=liked
        return  cumulative