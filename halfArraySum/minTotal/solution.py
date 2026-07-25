from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        for pile in piles:
            heappush(heap, -1 * pile) #want a max heap!
        

        for i in range(k):

            curr = abs(heappop(heap))

            numToRemove = curr // 2

            curr = curr - numToRemove

            heappush(heap, -1 * curr)
        
        return abs(sum(heap))





        
