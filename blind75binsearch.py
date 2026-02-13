class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''
        want to find the value where its greater than the index left and right of it
        '''

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right:
            
            mid = (right + left) // 2

            if nums[mid] > nums[right]:

                left = mid + 1

            else:

                right = mid
        
        return nums[left]


class Solution:
    def search(self, nums: List[int], target: int) -> int:


        '''
        binary search -> 
        what should the condition be that makes us update pointers

        '''

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:

                return mid


            if nums[left] <= nums[mid]:

                #mid is in left portion
                if target > nums[mid] or target < nums[left]:

                    #search right
                    left = mid + 1

                else:

                    right = mid - 1

            else: #mid is in the right portion

                if target < nums[mid] or target > nums[right]:

                    right = mid - 1
                
                else:

                    left = mid + 1 
            
        return -1
