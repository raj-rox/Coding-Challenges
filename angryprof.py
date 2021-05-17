#V easy. Solved on 1st attempt. DONE
#https://www.hackerrank.com/challenges/angry-professor/problem
def angryProfessor(k, a):
    # Write your code here
    #k is threshold number
    #a[n] is the arrival time
    count=0
    for i in a:
        if i<=0:
            count+=1
    if count>=k:
        return "NO"
    else:
        return "YES"