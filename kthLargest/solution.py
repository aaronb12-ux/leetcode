from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #create a heap a min heap of length k. this means that the top of the heap will always be the kth largest


        heap = []

        for num in nums:

            heappush(heap, num)

            if len(heap) > k:
                heappop(heap)
            
        return heappop(heap)
