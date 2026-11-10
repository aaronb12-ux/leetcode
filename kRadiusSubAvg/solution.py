class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:

        n = len(nums)
        ans = [-1] * n

        if 2 * k + 1 > n: #no valid bounds
            return ans
        
        curr_sum = sum(nums[:2 * k + 1])


        left = 0
        right = 2 * k

        for i in range(k, n - k):

            ans[i] = curr_sum // (2 * k + 1)

            curr_sum -= nums[left]
            left += 1

            right += 1
            if right < n:
                curr_sum += nums[right]
        
        return ans



        
