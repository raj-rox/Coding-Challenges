Problem: https://www.hackerrank.com/challenges/array-left-rotation/problem

def LR(a,n):
	temp=a.pop(0)
	a.append(temp)		
a=[1,2,3,4,5]
n=5
d=4
while(d!=0):
	LR(a,n)
	d-=1
for i in a:
	print(i,end=" ")
