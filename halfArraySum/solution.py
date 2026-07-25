from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        heap = []
        targetSum = sum(nums) / 2
        heapSum = sum(nums)
        count = 0

        for num in nums:
            heappush(heap, -1 * num) #want a max heap
        
      
        while heapSum > targetSum:
            
            curr = abs(heappop(heap))

            halfCurr = curr / 2

            heappush(heap, -1 * halfCurr)

            heapSum = abs(heapSum) - halfCurr
          
            count += 1
        
        return count
        
