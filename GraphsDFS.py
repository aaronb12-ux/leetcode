from collections import defaultdict
class dfsGRAPHS:

    def numberOfProvinces(self, isConnected: List[List[int]]) -> int:

        def makeAdjList():

            n = len(isConnected)
            adjList = defaultdict(list)

            for i in range(n):
                for j in range(n):
                    if isConnected[i][j] == 1:
                        adjList[i + 1].append(j + 1)
            
            return adjList
        
        def dfs(node):
            for neighbor in adjList[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        adjList = makeAdjList()
        seen = set()
        ans = 0

        for node in adjList:
            if node not in seen:
                ans += 1
                seen.add(node)
                dfs(node)
        
        return ans
    
    def numberOfIslands(self, grid: List[List[int]]) -> int:

        def isValid(row, col):
            return 0 <= row <= numRows and 0 <= col <= numCols
        
        def dfs(row, col):

            for dy, dx in directions:
                rowChange = row + dy
                colChange = col + dx

                if isValid(rowChange, colChange):
                    if (rowChange, colChange) not in seen and grid[rowChange][colChange] == "1":
                        seen.add((rowChange, colChange))
                        dfs(rowChange, colChange)
                        
        numRows = len(grid)
        numCols = len(grid[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)] #down, up, right, left
        seen = set()
        ans = 0

        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    seen.add((row, col))
                    ans += 1
                    dfs(row, col)
        return ans
    
    def minReOrder(n, connections): 

        roads = set()
        graph = defaultdict(list)

        for org, dest in connections:

            graph[org].append(dest)
            graph[dest].append(org)
            roads.add((org, dest))

        
        def dfs(city):
            ans = 0
            for neighbor in graph[city]:

                if neighbor not in seen:
                    if (city, neighbor) in roads:
                        ans += 1
                    
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            
            return ans
        
        seen = {0}
        return dfs(0)
    

    def unlockRoooms(rooms):

        def dfs(currentRoom):

            for key in rooms[currentRoom]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)

        visited = {0}
        dfs(0)
        return len(visited) == len(rooms)
    
    def validPath(n, source, destination, edges): #find if there is a valid path from source to dest

        def makeAdjList():

            adjList = defaultdict(list)

            for e1, e2 in edges:

                adjList[e1].append(e2)
                adjList[e2].append(e1)
            
            return adjList

        def dfs(o):
            #run dfs on origina (o) if we come across the destination, return true
            for neighbor in adjList[o]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor):
                        return True
            return False

        if source == destination:
            return True
         
        adjList = makeAdjList()
        visited = set()
        ans = dfs(source)
        
        return ans
