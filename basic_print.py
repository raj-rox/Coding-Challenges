https://www.hackerrank.com/challenges/python-print/problem
if __name__ == '__main__':
    n = int(input())
    ans=""
    while n:
        ans=str(n)+ans
        n=n-1
    print(int(ans))
