https://www.hackerrank.com/challenges/python-lists/problem?h_r=profile

if __name__ == '__main__':
    # T=input().split()
    L=[]
    for t in range(int(input())):
        args=input().strip().split(" ")
       # print(args)
        if args[0]=="append":
            L.append(int(args[1]))
        elif args[0]=="insert":
            L.insert(int(args[1]), int(args[2]))
        elif args[0]=="remove":
            L.remove(int(args[1]))
        elif args[0]=="pop":
            L.pop()
        elif args[0]=="sort":
            L.sort()
        elif args[0]=="reverse":
            L.reverse()
        elif args[0]=="print":
            print(L)