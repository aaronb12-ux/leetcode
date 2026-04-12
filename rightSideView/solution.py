from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #implement BFS and get nodes at each level. then append the last added node for the current level

        '''
        queue = deque([root])

        while the queue is not empty:

            currentLevel = len(queue)
            ans.append(queue[currentLevel - 1]) #most right node
            for node in current Level:
                pop from the queue
                    add its left and right neighbors
            
        '''

        if not root:
            return []
        
        ans = []
        queue = deque([root]) #queue is initialized with the root only

        while queue:

            levelLength = len(queue)

            ans.append(queue[levelLength - 1].val)

            for _ in range(levelLength):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return ans


        
