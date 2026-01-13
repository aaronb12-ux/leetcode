def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(len(nums)):
            curr = 1

            if i == len(nums) - 1: #last element
                allNums = nums[:i] #everything excluding the last element

            else:
                first_half = nums[:i]
                second_half = nums[i + 1:]
                allNums = first_half + second_half

            for num in allNums:
                curr = curr * num

            ans.append(curr)
    
        return ans
