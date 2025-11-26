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
    
    def deepestLeavesSum(root): #return sum of all leaves in deepest level

        if not root:
            return []
        
        levels = []
        queue = deque([root])

        while queue:

            levelLength = len(queue) #nodes in current level

            currentLevel = list(map(lambda node: node.val, queue))

            levels.append(currentLevel)

            for _ in range(levelLength):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return sum(levels[-1])
    
    def zigzagLevelOrderTraversal(root):

        if not root:
            return []
        
        levels = []
        queue = deque([root])
        currentLevel = 0

        while queue:

            levelLength = len(queue)

            level = list(map(lambda node: node.val, queue))

            if currentLevel % 2 != 0: #is ODD
                levels.append(level[::-1]) #reverse the level
            else:
                levels.append(level)
            
            for _ in range(levelLength):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            currentLevel += 1
        
        return levels






