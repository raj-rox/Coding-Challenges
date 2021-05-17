#Stack question :() Needed Bagde help. Redo.
#https://www.hackerrank.com/challenges/reduced-string/submissions/code/212065928    
    if s is None or "":
        return "Empty String"
    stack=[]
    for i in s:
        if stack:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i) 
        else:
            stack.append(i)
    if stack:
        x="".join(stack)
        return x
    else:
        return "Empty String"