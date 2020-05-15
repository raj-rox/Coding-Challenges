def Reversor(str):
    rev=""
    word=list(str)
    word.pop()
    n=len(word)
    while(n>0):
        rev = rev  + word.pop()
        n=n-1
    return rev
ans=repr(Reversor("Hell\0")+"\0")
print(ans)

#In python strings are immutable. So can't do it "in place". That extra place will have to be used unfortunately.
#It can be done using slicing word[::-1]. However, that is also O(n+k) complexity.
