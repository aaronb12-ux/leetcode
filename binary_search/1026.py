# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.answer = 0

        def dfs(node, currentMax, currentMin):
                    
            if not node:
                return 0
            
            currentMax = max(node.val, currentMax)
            currentMin = min(node.val, currentMin)
                  
            self.answer = max(self.answer, abs(currentMax - currentMin)) #update answer at each node
 
            dfs(node.left, currentMax, currentMin)
            dfs(node.right, currentMax, currentMin)
            
        
            return self.answer
        
        
        return((dfs(root, float("-inf"), float("inf"))))
            
