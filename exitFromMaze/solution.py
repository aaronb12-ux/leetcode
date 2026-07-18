from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
            run a bfs from where we begin
            if we try to move any direction and its a wall, dont move there. if yes, then move there
            and keep track of steps taken at that point

        '''


        m = len(maze) #num rows
        n = len(maze[0]) #num cols
        directions = [(1,0), (-1,0), (0,1), (0,-1)] #down, up, right, left
        queue = deque([(entrance[0], entrance[1], 0)]) 
        visited = {(entrance[0], entrance[1])}

        def inBounds(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def isExit(row, col):
            for dr, dc in directions:
                if not inBounds(row + dr, col + dc):
                    return True

        while queue:
        
            row, col, steps = queue.popleft()
           
            if isExit(row, col) and [row, col] != entrance:
                return steps 
            
            for dr, dc in directions:
                nextRow = row + dr
                nextCol = col + dc

                if inBounds(nextRow, nextCol):
                    if maze[nextRow][nextCol] != '+':
                        if (nextRow, nextCol) not in visited:
                            visited.add((nextRow, nextCol))
                            queue.append((nextRow, nextCol, steps + 1))
        

        return -1
                        
