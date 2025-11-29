class BinarySearchTrees:

    def inOrder(self, root): #get nodes in SORTED order

        if not root:
            return

        self.inOrder(root.left)
        print(root.val)
        self.inOrder(root.right)
    
    def preOrder(self, root): #start at root. then visit left subtree then right

        if not root:
            return
        
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):

        if not root:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)


    def minAbsDifference(self, root): #find minimum differnece between two nodes in BST

        def inOrder(node, sortedNodes):

            if not node:
                return
            
            inOrder(node.left, sortedNodes)
            sortedNodes.append(node.val)
            inOrder(node.right, sortedNodes)

            return sortedNodes
        
        sortedNodes = inOrder(root, [])

        left = 0
        right = 1
        ans = float("int")

        while right < len(sortedNodes):

            ans = min(ans, abs(sortedNodes[right]) - abs(sortedNodes[left]))
            right += 1
            left += 1
        
        return ans
    

    def rangeSum(self, root, low, high):   #given BST, return all nodes in the range (inclusive) from high to low

        if not root:
            return 0
        
        ans = 0
        
        if low <= root.val <= high:
            ans += root.val
        
        if root.val < high:
            ans += self.rangeSum(root.right, low, high)
        
        if root.val > low:
            ans += self.rangeSum(root.left, low, high)
        
        return ans
