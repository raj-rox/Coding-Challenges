def string_to_int(s):
    is_negative=1
    if(s[0]=='-'):
        is_negative=-1
        s.pop(0)
    result=0
    for i in range(len(s)):
        result*=10
        result+=int(s[i])
    return result*is_negative





s="314"
print(string_to_int(s))
