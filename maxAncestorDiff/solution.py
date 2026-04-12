# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
            
            def dfs(node, currmax, currmin):

                if not node: #
                    return abs(currmax - currmin)
                
                if node.val > currmax:
                    currmax = node.val
                
                if node.val < currmin:
                    currmin = node.val
           
                left = dfs(node.left, currmax, currmin)
                right = dfs(node.right, currmax, currmin)

                return max(left, right)
      
            return (dfs(root, float("-inf"), float("inf")))
