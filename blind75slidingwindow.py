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

