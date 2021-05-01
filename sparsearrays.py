#https://www.hackerrank.com/challenges/sparse-arrays/problem
def matchingStrings(strings, queries):
	# ans=[]
	# for i in queries:
	# 	#count of frequencies in strings.
	# 	count=0
	# 	for j in strings:
	# 		if i==j:
	# 			count+=1
	# 	ans.append(count)		
	# ans.sort(reverse=True)
	# return ans
	words=dict()
	ans=[]
	#queries are unique. check queries' in strings
	for w in strings:
		if w in words:
			words[w]+=1
		else:
			words[w]=1
	for q in queries:
		if q in words:
			ans.append(words[q])
		else: 
			ans.append(0)
	return ans

strings=["ab","bc","abc"]
queries=["ac","ab","abc"]
res = matchingStrings(strings, queries)
print(res)