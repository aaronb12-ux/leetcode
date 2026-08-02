import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        '''
        solution space problem: there is a threshold that makes all values below it false, and all values above it true. this is the case for this problem because we need to find the minimum positive. so we keep

        if minium is x, that means everything above x is true and we will make it on time, but its not the min

        this problem requires a binary search on the solution space, where the solution space being the speeds in k per hour
        '''


        def makeItInTime(speed):
            hoursTaken = 0

            for i in range(len(dist)):

                if i == len(dist) - 1:
                    #final train. No need to wait for the integer next hour
                    hoursTaken += dist[i] / speed
                else:
                    hoursTaken += math.ceil(dist[i] / speed)
            
            return hoursTaken <= hour

        
        '''
        1 3 2

        1 2 3   hour = 2.7


        middle = 2

        hoursTaken = math.ceil(1 / 2) -> 1



        '''

            
        left = 1
        right = 10**9
        best = -1
        
        while left <= right:

            middle = (left + right) // 2

            if makeItInTime(middle):
                #check smaller values
                print('here')
                best = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return best
        
