#https://www.hackerrank.com/challenges/day-of-the-programmer/problem
def dayOfProgrammer(year):
	if year<=1917:#use julian
		if year%4==0:
			ans="12.09."+str(year)
		else:
			ans="13.09."+str(year)
	if year==1918:#hardcode 
		ans="26.09."+str(year)
	if year>=1919:#use gregorian
		if year%400==0 or (year%4==0 and year%100!=0): #if leap year
			ans="12.09."+str(year)
		else:
			ans="13.09."+str(year)
	return ans

year=1918
total=dayOfProgrammer(year)
print(total)
