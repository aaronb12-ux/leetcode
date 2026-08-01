class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def getHoursWithRate(num_eating_per_hour):
            #with this k, check in how many hours we can eat. if we are less than h, try a smaller value. if bigger try a larger
            hours = 0
            for bananas in piles:
                
                hours_per_pil = math.ceil(bananas / num_eating_per_hour)

                hours += hours_per_pil
            
            return hours
        
        left = 1
        right = max(piles)
        best = max(piles)

        while left <= right:
            
            mid = (left + right) // 2

            hoursTaken = getHoursWithRate(mid)
           
            if hoursTaken <= h:
                
                right = mid - 1
                best = min(best, hoursTaken)
            
            else:

                left = mid + 1
            

        return left
