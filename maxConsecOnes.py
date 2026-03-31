class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        '''
                inputs: nums (array of nums)

                outputs: number of max ones in nums
        '''
        
        leftPtr = 0
        maxNum = 0
        numberZeros = 0

        for rightPtr in range(len(nums)):

            if nums[rightPtr] == 1:

                maxNum = max(maxNum, rightPtr - leftPtr + 1)

            else: #hit a zero

                while leftPtr <= rightPtr:

                    leftPtr += 1
        
        return maxNum
