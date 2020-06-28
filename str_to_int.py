def string_to_int(a):
    ans=0
    for digit in a:
        digitValu=ord(digit)-ord('0')
        ans=ans*10
        ans=ans+digitValu
    return ans

a="1225"
print(string_to_int(a))
