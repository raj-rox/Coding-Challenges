#https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
def insertNodeAtHead(llist, data):
    # Write your code here
    node1=SinglyLinkedListNode(data)
    if llist==None:
        llist=node1
        return llist
    else:
        node1.next=llist
        return node1