#Got it in the end khudse :). Question is not incorrect.
#https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?isFullScreen=false

def insertNodeAtTail(head, data):
    current=head
    if current:
        while  current.next:
            current=current.next
        x=SinglyLinkedListNode(data)
        current.next=x
    else:
        x=SinglyLinkedListNode(data)
        return x
    return head
