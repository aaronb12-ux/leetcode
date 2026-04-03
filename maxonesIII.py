class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        ans = 0
        numZeros = 0
        leftPtr = 0
        
        for rightPtr in range(len(nums)):
            
            if nums[rightPtr] == 0:
                    numZeros += 1
                
            while numZeros > k:
                    if nums[leftPtr] == 0:
                        numZeros -= 1
                    leftPtr += 1
                
            ans = max(ans, rightPtr - leftPtr + 1)
        
        return ans
        
        
