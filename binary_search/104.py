# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #RECURSIVE SOLUTION
        def dfs_recursive(root):

            if root == None:
                return 0
            
            left_depth = dfs(root.left) #finds longest left subtree
            right_depth = dfs(root.right) #finds longest right subtree

            return 1 + max(left_depth, right_depth)
          
        
        depth = dfs_recursive(root)

        return depth
        

        #ITERATIVE SOLUTION
        def dfs_iterative():

            if not root:
                return 0

            ans = 0
            stack = [(root, 1)]

            while stack:

                node, depth = stack.pop()
                
                ans = max(ans, depth)

                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))
                
            return ans
        

        ans = dfs_iterative()
        return ans
