from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        '''
        shortest path -> BFS

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        at each position we are in, we need to keep track of the number of steps we have taken, the position, and number of eliminations we have. We can only visited a node if we have steps left and we havent visited it yet
        '''

        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] #left, right, up, down
        queue = deque([(0, 0, k, 0)]) #row, col, eliminations, steps taken
        visited = set((0, 0, k))

        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols

        while queue:

            row, col, elim, steps = queue.popleft()
            print(steps)
            if row == rows - 1 and col == cols - 1: #at the end
                return steps

            for dx, dy in directions:
                nextRow = row + dx
                nextCol = col + dy

                if valid(nextRow, nextCol):
                    if grid[nextRow][nextCol] == 1:
                        if elim > 0 and (nextRow, nextCol, elim - 1) not in visited:
                            visited.add((nextRow, nextCol, elim - 1))
                            queue.append((nextRow, nextCol, elim - 1, steps + 1))
                    else:
                        if (nextRow, nextCol, elim) not in visited:
                            visited.add((nextRow, nextCol, elim))
                            queue.append((nextRow, nextCol, elim, steps + 1))
        
        return -1


        
