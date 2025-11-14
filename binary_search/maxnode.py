# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxNodeInTree(self, root: Optional[TreeNode]) -> int:

        def maxnode(node, currentMax):
            
            if not node:
                return 0
            
            if node.val > currentMax:
                currentMax = node.val

            left = maxnode(node.left, currentMax)
            right = maxnode(node.right, currentMax)
            
            return max(left,right,node.val)
        
        print(maxnode(root, float("-inf")))
