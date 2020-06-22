x='101010101'
ones=0
for i in x:
    if i=='1':
        ones=ones+1
    x=int(x)
    x&=x-1#TRICK makes it O(k)
    x=str(x)

if ones%2 == 0:
    print("Parity is 0")
elif ones%2 ==1:
    print("Parity is 1")
    
 #ForO(log(n))exploit ^ and the fact it's 64 bit data. 32,16,8,4,2,1...exor & right shift twice.
