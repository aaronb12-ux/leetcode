class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        '''
            input: 
                nums -> array of nums
                k -> constraint
            
            output:
                number of contiguous subarrays in nums that have product less than k

        '''
        if k == 0 or k == 1:
            return 0

        leftPtr = 0
        ans = 0
        currentWindowProduct = 1

        for rightPtr in range(len(nums)):

            currentWindowProduct *= nums[rightPtr]
            
            while currentWindowProduct >= k:

                currentWindowProduct = currentWindowProduct // nums[leftPtr]

                leftPtr += 1
            
            ans += rightPtr - leftPtr + 1
        
        return ans
        
