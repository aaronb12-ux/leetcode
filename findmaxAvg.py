class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ans = 0
        currentSum = 0
        
        for rightPtr in range(k):
            currentSum += nums[rightPtr]
        
        ans = currentSum / k
        leftPtr = 0
        
        for rightPtr in range(k, len(nums)):
            currentSum = currentSum + nums[rightPtr] - nums[leftPtr]
            
            currentSumAvg = currentSum / k
            
            
            ans = max(ans, currentSumAvg)
            
            print(ans)
            
            leftPtr += 1
        
        return ans
        
