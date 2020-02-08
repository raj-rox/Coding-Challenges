This is the code for:https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

a=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
S=15
for i in range(0,5):
	sum=a[i]
	j=i+1
	while((sum < S+1) and (j<len(a))):
		sum=sum+a[j]
		if(sum==S):
			print(i+1, end=" ")
			print(j+1)
		j+=1
