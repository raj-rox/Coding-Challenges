#https://www.hackerrank.com/challenges/electronics-shop/problem
def getMoneySpent(keyboards, drives, b):
	keyboards.sort(reverse=True)
	drives.sort()
	ans=0
	for x in keyboards:
		for y in drives:
			if x+y>b:
				break
			if ans<(x+y):
				ans=x+y
	if ans==0:
		return -1
	else
		return ans
keyboards=[3,1,5,3,2]
drives=[5,2,8,4,2,5,7]
b=10
moneySpent = getMoneySpent(keyboards, drives, b)
print(str(moneySpent))
