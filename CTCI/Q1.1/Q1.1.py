flag=0
a="abcdb"
for i in range(0,len(a)):
    for j in range(i+1, len(a)):
        if(a[i]==a[j]):
            print("Not Unique")
            flag=1
if(flag==0):
    print("Unique")
print(len(a))
