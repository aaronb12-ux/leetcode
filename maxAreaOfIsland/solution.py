class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

   
        visited = set()
        ans = []
        self.currArea = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #down up right left
        m = len(grid)
        n = len(grid[0])


        def valid(row, col):

            return 0 <= row < m and 0 <= col < n


        def dfs(row, col):
            
            for dy, dx in directions:
                nextRow = row + dy
                nextCol = col + dx

                if valid(nextRow, nextCol) and (nextRow, nextCol) not in visited:

                    if grid[nextRow][nextCol] == 1:

                        visited.add((nextRow, nextCol))
                        self.currArea += 1
                        dfs(nextRow, nextCol)
             
    
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    self.currArea += 1
                    visited.add((i, j))
                    dfs(i, j)
                    ans.append(self.currArea)
                    self.currArea = 0
                    
        if not ans:
            return 0
        return max(ans)
