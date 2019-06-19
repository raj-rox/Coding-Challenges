n=int(input("Enter the no of socks:"))
#print(n)
ar=[]#Set size acc to n
ar1=set()

print("Enter the sock colour nos:")
for i in range(0,n):
	ar.append(int(input()))
print("ar is:", ar)
i=0
sum=0
ar1=set(ar)#ar1 consists of the unique elements in ar
ar1=list(ar1)
count=[0]*len(ar1)
for i in range(0,len(ar1)):
	for j in range(0,n):
		if ar1[i] == ar[j]:
			count[i]+=1

print("ar1 is:", ar1)
print("The count is:", count)
for i in range(0,len(ar1)):
	count[i]=int(count[i]/2)
	sum=sum+count[i]
print("The count is:", count)
print("The no of pairs are:", sum)
