class BST:
  
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        #traverse the tree and only count values within the range

        if not root:
            return 0
        ans = 0
        if low <= root.val <= high:
            ans += root.val
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high) #current node is greater than low, there might still be some lower nodes in range to the left
        if root.val < high:
            ans += self.rangeSumBST(root.right, low, high) #current node is less than the high, there might still be some nodes to the range on the right

        return ans
