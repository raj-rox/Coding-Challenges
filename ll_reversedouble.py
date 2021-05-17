#Just used the single LL's stuff
def reverse(llist):
    # Write your code here
    if llist==None:
        return
    else:
        prev=None
        while llist:
            temp=llist
            llist=llist.next
            temp.next=prev
            prev=temp
        return prev