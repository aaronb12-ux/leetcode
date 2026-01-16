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


 def longestConsecutive(self, nums: List[int]) -> int:
        
        #iterate through all the numbers

        '''
            for each number we check if num + 1 is in numsSet
            if yes, we incrament our current answer and then again check if that number + 1 is in nunsSet. we continue until this return false
            and if false we return the current count and update our global max
        '''
        if not nums:
            return 0

        numsSet = set(nums)
        current = 0
        globalMax = 0 

        for num in nums:

            while True:

                if num + 1 in numsSet:
                    current += 1
                    num = num + 1
                else:
                    globalMax = max(current, globalMax)
                    current = 0
                    break
        
        return globalMax + 1


def isPalindrome(self, s: str) -> bool:
        
        #remove all white space in the string
        #remove all non alphanumerica characters and digits
        #do normal palindrome check

        noSpaces = s.replace(" ", "")

        for char in noSpaces:

            if not char.isalnum(): 

                noSpaces = noSpaces.replace(char, "")
        
        validString = [char.lower() for char in noSpaces]

        res = ''.join(validString)


        left = 0
        right = len(res) - 1

        while left <= right:

            if res[left] != res[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
