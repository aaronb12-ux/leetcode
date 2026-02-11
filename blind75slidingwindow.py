class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        seen = set()
        ans = 0

        for num in prices:

            if not seen:
                seen.add(num)
            else:
                ans = max(ans, num - min(seen))
                seen.add(num)
        
        return ans


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        currentWindow = set()
        ans = 0


        if len(s) == 1:
            return 1

        while left < len(s) and right < len(s):
    
            if s[right] not in currentWindow:
                currentWindow.add(s[right])
                ans = max(ans, right - left + 1)
                right += 1
                print(ans)
               
            else:
                while s[right] in currentWindow:
                    currentWindow.remove(s[left])
                    left += 1
                   

        return ans


from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def mostFrequent():

            maxFreq = 0

            for key in currentWindow:

                maxFreq = max(maxFreq, currentWindow[key])

            return maxFreq

        left = 0
        currentWindow = defaultdict(int)
        ans = 0

        for right in range(len(s)):

            currentWindow[s[right]] += 1

            windowSize = right - left + 1
            
            if windowSize - mostFrequent() <= k: #valid window

                ans = max(windowSize, ans)
            
            while (right - left + 1) - mostFrequent() > k:
       
                currentWindow[s[left]] -= 1

                left += 1
            
            if right == len(s) - 1:
                
                return max(ans, right - left + 1)
            
        return ans

