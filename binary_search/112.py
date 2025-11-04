# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        #iterative solution:

        
        implement a stack approach
        initialize a stack with the root and each element of the stack is a tuple: [node, path_sum]
        do normal while loop and for each iteration check if path_sum == target and return true
        if we make it out of the while loop, return False
        
        def iterative_dfs():

            if not root:
                return False

            stack = [(root, root.val)]

            while stack:

                node, current_path_sum = stack.pop()

                if (not node.left) and (not node.right) and current_path_sum == targetSum:
                    return True
                
                if node.left:
                    stack.append((node.left, current_path_sum + node.left.val))
                if node.right:
                    stack.append((node.right, current_path_sum + node.right.val))
            
            return False

        return(iterative_dfs())
        


        def recursive_dfs(root, current_sum):

            if not root:
                return False
            
            if root.left == None and root.right == None:

                return current_sum + root.val == targetSum
            
            return recursive_dfs(root.left, current_sum + root.val) or recursive_dfs(root.right, current_sum + root.val)
          
   
        
            
        return recursive_dfs(root, 0)
