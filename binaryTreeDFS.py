#Max Depth
class BinarySearchDFS:

    #finding max depth of binary tree
    def maxDepth(self, root):

        def height(node):

            if not node:
                return 0
        
            left = self.maxDepth(node.left)
            right = self.maxDepth(node.right)

            return 1 + max(left, right)
        
        return height(root)
    


    #finding the min depth of binary tree
    def minDepth(self, root):

        def mindepth(node):

            if not node:
                return 0
            
            left = self.mindepth(node.left)
            right = self.mindepth(node.right)

            if left == 0: #if no left subtree
                return 1 + right
            elif right == 0: #if no right subtree
                return 1 + left
            
            return 1 + min(left, right)

        return mindepth(root)
    

    #check if any root to leaf path sums to target
    def pathSum(self, root, target):

        def dfs(node, currentSum):

            if not node.left and not node.right: #hitting a leaf, check if we have found a pathsum
                return currentSum == target
            
            left = dfs(node.left, currentSum + node.val)
            right = dfs(node.right, currentSum + node.val)

            return left or right
        
        return(dfs(root, 0))
    
    
    #check how many good nodes exist in a binary tree. A node is a goodNode when on all ancestors of that node, the currentNodes value is greater than or equal to all of them
    def goodNodes(self, root):

        self.goodNodes = 0

        def dfs_global(node, maxNode): #GLOBAL VAR version

            if not node: #value of nothing is 0
                return 0
            
            if node.val >= maxNode:
                self.goodNodes += 1

            dfs_global(node.left, max(node.val, maxNode))
            dfs_global(node.right, max(node.val, maxNode))

        dfs_global(root, 0, float("-inf"))

        def dfs_pure(node, maxNode): #Pure dfs

            if not node:
                return 0
            
            left = dfs_global(node.left, max(node.val, maxNode))
            right = dfs_pure(node.right, max(node.val, maxNode))

            ans = left + right

            if node.val >= maxNode:
                ans = ans + 1

            return ans
        
        return(dfs_pure(root, float("-inf")))
    

    #find diameter of binary tree
    def diameter(self, root):

        self.max_diameter = 0

        def height(node): #returns the height of a subtree

            if not node: #height of nothing is 0
                return 0
                
            left = height(node.left)
            right = height(node.right)

            diameter = left + right

            self.max_diameter = max(self.max_diamter, diameter)

            return max(left, right) + 1
            
        height(root)
        return self.max_diamter
    
    #determine if two trees are the same
    def sametree(self, p, q):

        def dfs(node1, node2):

            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right
        
        return dfs(p, q)










