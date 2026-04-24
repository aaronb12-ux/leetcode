from collections import defaultdict
from collections import deque
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        
        def makeAdjList():
            adjList = defaultdict(list)

            for u, v in edges:
                adjList[u].append(v)
                adjList[v].append(u)
            

            return adjList
        

        adjList = makeAdjList()
        restrictedSet = set(restricted)
        queue = deque([0])
        visited = {0}
        self.ans = 1

        def bfs(start):

            while queue:

                currentNode = queue.popleft()

                for neighbor in adjList[currentNode]:
                    print(neighbor)
                    if neighbor not in restrictedSet and neighbor not in visited:

                        self.ans += 1
                        queue.append(neighbor)
                        visited.add(neighbor)
        
        bfs(0)

        return self.ans
