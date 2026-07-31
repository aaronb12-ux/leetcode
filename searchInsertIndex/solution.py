class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        '''
            run a binary search on the array. Continue until we find the target. return the index of that target

            [1, 3, 5, 6] target = 7

            l = 0 
            r = 3

            middle = 1

            l = 2
            r = 3

            middle = 2 

            l = 3
            r = 3

            middle = 3


        '''

        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return left
