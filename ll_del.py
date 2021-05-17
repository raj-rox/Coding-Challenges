#Done at 1st try
#https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    # x=SinglyLinkedListNode(data)
    if head==None and position==0:
        return None
    if position==0 and head:
        ptr=head.next
        return ptr
    if position and head:
        ptr=head
        while position!=1:
            ptr=ptr.next
            position-=1
        # x.next=ptr.next
        # ptr.next=x
        # return head
        ptr.next=ptr.next.next
        return head
if __name__ == '__main__':