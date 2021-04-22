#https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q=[]
        q.append([])
        while len(q)!=0:
	        value=q.pop(0)
	        if value.left:
	        	q.append(value.left)
	        if value.right:
	        	q.append(value.right)
	        print(value.val)
        return []    #20 9



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q=[]
        q.append(root)
        while len(q)!=0:
            # print("length of q is:",len(q))
            size=len(q)#No of parent elements
            for i in range(0, size):
                value=q.pop(0)
                if value.left:
                    q.append(value.left)
                if value.right:
                    q.append(value.right)
                print(value.val)    
            print("----")
        return []    
