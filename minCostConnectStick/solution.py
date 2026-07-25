from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        '''
                utilize a max heap
                and continue to iterate until there is one stick left

                for each iteration pop sticks 0 and 1 from the heap. combine them. then insert back into heap
        '''

        heap = []
        minCost = 0
        for stick in sticks:
            heappush(heap, stick)
        
        if len(heap) == 1: #only the one stick exists so return it
            return 0
        
        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)

            combine = x + y
            minCost = minCost + combine
            heappush(heap, combine)
        
        return minCost
