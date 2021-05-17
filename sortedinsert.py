#Couldnt debug :/. Try again on weekend?
#https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

def sortedInsert(llist, data):
    # Write your code here
    if llist is None:
        x=DoublyLinkedListNode(data)
        return x
    current=llist
    while current:
        if data>=(current.next).data:
            break
        current=current.next
    temp=current.next
    x=DoublyLinkedListNode(data)
    current.next=x
    x.prev=current
    x.next=temp
    temp.prev=x
    return llist