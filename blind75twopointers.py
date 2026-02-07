class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        nums.sort()

        #outer loop -> checks each number in nums
        for i in range(len(nums)):

            left = i + 1
            right = len(nums) - 1

            while left < right: #this continue until left hits right pointer. when this happens reset pointers and iterate the for loop

                #skip duplicates
                if left == i:
                    left += 1
                if right == i:
                    right -= 1

                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == 0 and tuple([nums[i], nums[left], nums[right]]) not in seen:
                    ans.append([nums[i], nums[left], nums[right]])
                    seen.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1

                elif currentSum < 0: #sum is less than 0 -> need to find larger numbers -> move left pointer to the right?
                    left += 1
                
                else: #sum is greater than 0, need to move right pointer to find smaller values
                    right -= 1

        return ans
        
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:

            curr_water = (right - left) * min(heights[left], heights[right])

            if curr_water > max_water:
                max_water = curr_water

            #move the smaller height because we want to search for a taller height to fit more water from now on
            if heights[right] > heights[left]:
                left += 1
            
            elif heights[right] < heights[left]:
                right -= 1
            
            else:
                left += 1
                right -= 1
            
        return max_water

