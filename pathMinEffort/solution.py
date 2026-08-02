from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        '''
        get all paths with a bfs
        at the end get the max of all the paths, and return the mid of that
        '''
        m = len(heights)
        n = len(heights[0])
        def valid(row, col):

            return 0 <= row < m and 0 <= col < n


        def bfs(middle):

            queue = deque([(0,0)]) #queue stores coordinates
            visited = {(0,0)} 
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                
                row, col = queue.popleft()
                print(row, col)
                if (row, col) == (m - 1, n - 1):
                    
                    return True
                
                for dy, dx in directions:
                    nextRow = row + dy
                    nextCol = col + dx

                    if valid(nextRow, nextCol):
                        if (nextRow, nextCol) not in visited:
                            
                            if abs(heights[row][col] - heights[nextRow][nextCol]) <= middle:
                                queue.append((nextRow, nextCol))
                                visited.add((nextRow, nextCol))
    
        left = 0
        right = max(max(row) for row in heights)
        currBest = None
        while left <= right:

            middle = (right + left) // 2

            #run a bfs with the middle and check if we can find a path where the highest change is at most middle. if this is ture, then set currentBest to middle and check smaller values

            if bfs(middle):
                right = middle - 1
                currBest = middle
            
            else:
                left = middle + 1

        return currBest




        
