# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #implement dfs 
        ans = 0

        def dfs(node, max_so_far):

            if not node:
                return 0

            #max_so_far is the max of the current path
            leftPath = dfs(node.left, max(max_so_far, node.val))
            
            rightPath = dfs(node.right, max(max_so_far, node.val))

            ans = leftPath + rightPath

            if node.val >= max_so_far:
                ans += 1
            
            return ans

            
        return dfs(root, float("-inf"))
