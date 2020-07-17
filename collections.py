https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: #No need for exists & checking >0.Seedha do this. 
        income += price#Nai hua toh it won't return some value. Jude stylee
        shoes[size] -= 1

print(income)
