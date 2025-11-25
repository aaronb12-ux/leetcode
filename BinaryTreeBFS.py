from collections import deque
class BinaryTreeBFS:

    def generalFormat(root): #general format for many Binary Tree BFS problems

        queue = deque([root])

        while queue:

            nodes_in_current_level = len(queue)

            #do something for current level

            for _ in range(nodes_in_current_level):
                
                node = queue.popleft()

                #do logic for current node
                print(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
    def rightSideView(root): #return all right side nodes of a binary tree (assume standing on the right side of the tree and look at it)

        if not root:
            return []

        ans = []

        queue = deque([root])

        while queue:

            levelLength = len(queue) 

            ans.append(queue[-1].val)

            for _ in range(levelLength): #need to traverse all nodes on the current level

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
    
    def largestLevelValue(root): #return all max values for each level of binary tree

        if not root:
            return []
        
        ans = []

        queue = deque([root])

        while queue:

            levelLength = len(queue)

            levelValues = list(map(lambda node: node.val, queue))
            ans.append(max(levelValues))

            for _ in range(levelLength):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
