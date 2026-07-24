from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
            implicit graph problem
            a genes neighbors are all possible changes of the current Gene
        '''
        
        queue = deque([(startGene, 0)])
        geneBank = set(bank)
        seen = {startGene}

        def getGeneNeighbors(gene):
            print(gene)
            neighbors = []

            for i in range(len(gene)):
                a = gene[:i] + "A" + gene[i + 1:]
                c = gene[:i] + "C" + gene[i + 1:]
                g = gene[:i] + "G" + gene[i + 1:]
                t = gene[:i] + "T" + gene[i + 1:]
                print(a, c, g, t)
                if a in bank:
                    neighbors.append(a)
                if c in bank:
                    neighbors.append(c)
                if g in bank:
                    neighbors.append(g)
                if t in bank:
                    neighbors.append(t)
            print(neighbors)
            return neighbors

        while queue:

            gene, steps = queue.popleft()
            
            if gene == endGene:
                return steps
            
            neighborsOfGene = getGeneNeighbors(gene)
            print(neighborsOfGene)
            for neighbor in neighborsOfGene:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1
