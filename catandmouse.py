#Chindhi
#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
    if abs(y-z)==abs(x-z):
        return("Mouse C")
    elif abs(y-z)>abs(x-z):
        return("Cat B")
    elif abs(y-z)<abs(x-z):
        return("Cat A")

x=1
y=2
z=3
result = catAndMouse(x, y, z)
print(result)
