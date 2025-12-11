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
