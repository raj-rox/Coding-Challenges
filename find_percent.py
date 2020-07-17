https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=profile

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_scores=student_marks[query_name]
    ans=0.00
    for marks in query_scores:
        ans+=float(marks)
    print('{0:.2f}'.format(ans/len(query_scores)))


