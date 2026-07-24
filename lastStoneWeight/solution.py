from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        stones = [2, 7, 4, 1, 8, 1]

        turn 1: 7 and 8 
                8 > 7 -> smash and 8 becomes 1 
                now [2, 4, 1, 1, 1]
        turn 2: 4 and 2 -> smash and 4 becomes 2
                now [2, 1, 1, 1]
        turn 3: 2 and 1 -> smash and 2 becomes 1
                now [1, 1, 1]
        turn 4: 1 and 1 -> smash both are destroted

        left with 1

        we keep a max heap and always smash the stones at index 0 and 1
        '''
        heap = []
        for num in stones:
            num = num * -1
            heappush(heap, num)
        
        while len(heap) >= 2: #continue until there are 1 or 0 elements left in the heap
            x = heappop(heap)
            y = heappop(heap)

            if x <= y:
                if x == y:
                    continue
                else:
                    y = abs(y) - abs(x)
                    heappush(heap, y)
        
        if heap:
            return abs(heappop(heap))
        else:
            return 0

