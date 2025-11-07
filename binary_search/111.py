# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        #do binary search. begin at root and traverse left and right subtree.
        #keep traversing and once we hit a leaf where the node.left == none and node.right == none, return the number of nodes we have seen until now
        
        def dfs(node):
                  
            if not node:
                return 0
                
            left = dfs(node.left)
            right = dfs(node.right)
                 
            if left == 0:
                return 1 + right
            elif right == 0:
                return 1 + left
    
            return 1 + min(left, right)
        
        return(dfs(root))
