import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        ceiling devision

        solution space: minimum is lowest in arr, max is greatest in arr

        check values in the solution space and see if less than thresh. if it is, then check smaller values
        ''' 
        def inThreshold(divisor):

            divSum = 0

            for num in nums:
                divSum = divSum + math.ceil(num / divisor)

            return divSum <= threshold

        left = 1
        right = max(nums)
        best = None

        while left <= right:

            middle = (left + right) // 2

            if inThreshold(middle):
                best = middle
                right = middle - 1

            else:
                left = middle + 1

        return best        
