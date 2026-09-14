from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
            
        ans = []
        
        def back_track(curr, node):
            
            if node == len(graph) - 1: #reached end node
                ans.append(curr[:])
                
            
            for neighbor in graph[node]:
                curr.append(neighbor)
                back_track(curr, neighbor)
                curr.pop()
        
        back_track([0], 0)
        
        return ans
                
                
