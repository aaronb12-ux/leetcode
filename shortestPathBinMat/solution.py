from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        '''
            BFS starting from top left. Add the top left to the queue at the start. 
                If the top left or bottom right is not 0, return -1
        '''

        n = len(grid)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        queue = deque([(0,0,1)]) #x pos, y pox, steps
        visited = set((0,0)) #contains coordinates we visited

        # edge cases

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        def inBounds(row, col):

            return 0 <= row < n and 0 <= col < n
        
        #do the bfs
        while queue:

            row, col, steps = queue.popleft()

            print(row, col, steps)

            if row == n - 1 and col == n - 1: 
                return steps
            
            for dx, dy in directions:
                 
                 nextRow = dx + row
                 nextCol = dy + col

                 if inBounds(nextRow, nextCol):
                    if (nextRow, nextCol) not in visited:
                        if grid[nextRow][nextCol] == 0:
                            visited.add((nextRow, nextCol))
                            queue.append((nextRow, nextCol, steps + 1))
        
        return -1
            

        
