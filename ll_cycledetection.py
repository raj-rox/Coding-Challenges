#2 pointer, cycle detection. Some small mistake somewhere. Weekend?
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
# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    ptr1=head
    ptr2=head
    count=0
    if head:
        while ptr2.next or ptr2:    
            ptr1=ptr1.next
            # count+=1
            ptr2=ptr2.next.next
            if ptr1==ptr2:   
                return 1
        return 0
    else:
        return 0    
    # int HasCycle(Node head) {
#     if (head == null){
#         return 0;
#     }

#     Node slow = head;
#     Node fast = head;

#     while (fast != null && fast.next != null){
#         slow = slow.next;
#         fast = fast.next.next;

#         if (slow == fast){
#             return 1;
#         }
#     }

#     return 0;
# }
        
        
if __name__ == '__main__':