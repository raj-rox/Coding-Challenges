#This is the solution for: https://www.hackerrank.com/challenges/2d-array/problem

def maxhourglass(a):
	count=0
	maxcount=-63
	for i in range(4):
		for j in range(4):
			count=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]	
			if(count>maxcount):
				maxcount=count
	return maxcount

a=[]
a=[[-9, -9, -9, 1, 1, 1],[0, -9,  0,  4, 3, 2],[-9, -9, -9,  1, 2, 3], [0,  0, 8,  6, 6, 0], [0,  0,  0, -2, 0, 0],[0,  0,  1,  2, 4, 0]]
value=maxhourglass(a)
print(value)
