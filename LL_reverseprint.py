# NEED TO SOLVE AGAIN. BARELY UNDERSTOOD IT.
#https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
#https://www.youtube.com/watch?v=XDO6I8jxHtA&ab_channel=FriendlyGardenSnake
def reverse(head):
    if head==None:
        return
    else:
        prev=None
        while head:
            temp=head
            head=head.next
            temp.next=prev
            prev=temp
        return prev
