# n=int(input("Enter the no of clouds:"))
n=7

# print("Enter the array c:")
#ele=0
# for i in range(0,n):
# 	ele=int(input())
# 	c.append(ele)
c=[0, 0, 0, 1, 0, 0]
soln=[]
c.append(2)
c.append(2)
print("The cloud array is:", c)
i=0
while(c[i+2] != 2):
	if c[i+2]==0:
		i=i+2
	elif(c[i+1]==0):
		i=i+1
	soln.append(i)
if c[i+1]==0:
	i=i+1
	soln.append(i)
print(soln)