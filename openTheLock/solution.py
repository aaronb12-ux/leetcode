from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
            minimum value -> bfs
            think of a graph where all consequent turns from one combination are neighbors
            we begin at our source which is 0000 and run a bfs to find the minimum path to the target

            hard part is getting the neighbors from a node -> that is done with a function

            start with the source
            get all its neighbors
            explore the neighbors of those neighbors and keep track of the steps we have taken
            then eventually if a neighbor is the target, return the number of steps

            if a neighbor is a deadend, dont explore that neighbor and add it to the neighbors

            example:
                0000 -> neighbors are 1000 0100 0010 0001 9000 0900 0090 0009

                basically each combo has 8 neighbors (if not in dead ends) we add one to all individual spots and substract 1 from all individual spots

                1000 -> neighbors a
        '''

        queue = deque([("0000", 0)])
        visited = {"0000"}

        if "0000" in deadends:
            return -1

        def getNeighbors(current):
            neighbors = []
            newCombo1 = ""
            newCombo2 = ""

            for i in range(0, 4): #index 0 - 3

                if current[i] == "0":
                #keep original but change the 0 -> 1 at current[i]
                #keep original but change the 0 -> 9 at current[i]
                    newCombo1 = current[:i] + "1" + current[i + 1:]
                    newCombo2 = current[:i] + "9" + current[i + 1:]
                
                elif current[i] == "9":
                    newCombo1 = current[:i] + "0" + current[i + 1:]
                    newCombo2 = current[:i] + "8" + current[i + 1:]

                else:
                    increase = int(current[i]) + 1
                    decrease = int(current[i]) - 1

                    newCombo1 = current[:i] + str(increase) + current[i + 1:]
                    newCombo2 = current[:i] + str(decrease) + current[i + 1:]

                if newCombo1 not in deadends:
                    neighbors.append(newCombo1)
                if newCombo2 not in deadends:
                    neighbors.append(newCombo2)

            return neighbors
           

        while queue:

            currentCombo, steps = queue.popleft()

            if currentCombo == target:
                return steps

            neighbors = getNeighbors(currentCombo)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, steps + 1))
                    visited.add(neighbor)
            neighbors = []
    
        return -1

'''
queue = 0000, 0
neighbors = 1000 0100 0010 0001 9000 0900 0090 0009
queue = 1000
'''
