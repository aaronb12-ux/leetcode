# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #perform an inorder traversal of each tree and add node values to list
        #if lists are the same, return true, if not false
        
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False

        
        left = self.isSameTree(p.left, q.left) #check if left subtrees are equal
        right = self.isSameTree(p.right, q.right) #check if right subtrees are equal

        return left and right
