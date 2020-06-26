def revword(s):
    s.reverse()
    for x in s:
        soln=s.pop(0)
        if x == ' ':
            soln.reverse()
            soln.append(" ")




s="Bob likes Alice"
revword(s)
