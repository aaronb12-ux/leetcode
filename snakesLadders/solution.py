from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        '''
            since we are finding the shortest number of rolls, do a BFS

            begin on square 1
            on each square, loop through [curr + 1, min(curr + 6, n^2)]
            this simulates each roll. If this lands on a snake or ladder, then move to the destination of it.
            each role adds a step to the current path

            this is not a grid problem where we check all directions. we move in one direction so a 'directions' array is not needed

            you can only take a single snake or ladder on one role.

            hardest part: the boustrophoden style graph and not taking more than one snake/ladder each role

            have a function that converts row, col to number

        '''
        
        n = len(board)
        visited = {1} #location
        queue = deque([(1, 0)]) #location, steps taken from start

        def numberToCoord(location):
            rowNum = (location - 1) // n
            colNum = (location - 1) % n

            if rowNum % 2 == 1:  # odd row: reverse direction
                colNum = n - 1 - colNum

            return rowNum, colNum

        while queue:
            
            location, steps = queue.popleft()
            
            if location == n * n: #at end
                return steps

            for destination in range(location + 1, min(location + 6, n * n) + 1):

                if destination not in visited:
                  
                    row, col = numberToCoord(destination) #from here check if we are at snake or ladder
                    python_row = n - 1 - row
                    if board[python_row][col] != -1:
             
                        queue.append((board[python_row][col], steps + 1))
                    
                    else:
                        queue.append((destination, steps + 1))

                    visited.add(destination)
        
        return -1
