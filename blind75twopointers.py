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
