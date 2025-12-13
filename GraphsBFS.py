class GraphsBFS:

    from collections import deque

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n

        n = len(grid) #n x n grid
        visited = set([(0,0)])
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,1), (1,1), (1,-1), (-1,-1)] 
        queue = deque([(0,0,1)])

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        while queue:
      
            row, col, steps = queue.popleft()
            
            if (row, col) == (n - 1, n - 1): #if we reach the end (bottom right)
                return steps
            
            for dy, dx in directions:
                nextRow = row + dy
                nextCol = col + dx

                if valid(nextRow, nextCol):
                    if grid[nextRow][nextCol] == 0:
                        if (nextRow, nextCol) not in visited:
                            visited.add((nextRow, nextCol))
                            queue.append((nextRow, nextCol, steps + 1))
        
        return -1

    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        #turn tree into a graph by forming an adj list of it
        #run a bfs starting from the target and capture all nodes k distance
        queue = deque([root])
        ans = []
        adjList = defaultdict(list)

        def makeAdjList(root):

            if not root:
                return

            while queue:

                currentNode = queue.popleft()

                if currentNode.left:
                    adjList[currentNode.val].append(currentNode.left.val)
                    adjList[currentNode.left.val].append(currentNode.val)
                    queue.append(currentNode.left)

                
                if currentNode.right:
                    adjList[currentNode.val].append(currentNode.right.val)
                    adjList[currentNode.right.val].append(currentNode.val)
                    queue.append(currentNode.right)
        
        makeAdjList(root)

        queue = deque([target.val])
        visited = {target.val}
        level = 0

        while queue:

            if level == k:
                return list(queue)

            levelLength = len(queue) #one node in the current level

            for _ in range(levelLength):

                currentNode = queue.popleft()

                for neighbor in adjList[currentNode]:

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                
            level += 1
        
        return []
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:


        m = len(mat) #num rows
        n = len(mat[0]) #num cols
        directions = [(1,0), (-1,0), (0,1), (0,-1)] #down, up, right, left
        queue = deque([])
        visited = set()
 
        for i in range(m): #initialize queue
            for j in range(n):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i, j, 0)) #append cell location and steps taken (0)
        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
                    
        while queue:

            row, col, steps = queue.popleft()

            if mat[row][col] == 1:
                mat[row][col] = steps
            
            for dy, dx in directions:
                nextRow = row + dy
                nextCol = col + dx

                if valid(nextRow, nextCol):
                    if (nextRow, nextCol) not in visited:
                        visited.add((nextRow, nextCol))
                        queue.append((nextRow, nextCol, steps + 1))
        
        return mat
