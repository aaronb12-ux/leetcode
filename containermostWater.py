class Solution:
    def maxArea(self, height: List[int]) -> int:

        '''
                inputs:
                    height: array of nums representing the heights
                output:
                    area that holds the most water
        
        algorithm:
            two pointer approach because we need to check two heights at a time
        
        data structures:
            array (given to use)
        '''

        leftPtr = 0
        rightPtr = len(height) - 1
        ans = 0

        while leftPtr < rightPtr:

            h = min(height[leftPtr], height[rightPtr])
            w = rightPtr - leftPtr

            ans = max(ans, h * w)

            if height[leftPtr] < height[rightPtr]:
                leftPtr += 1
            
            elif height[leftPtr] > height[rightPtr]:
                rightPtr -= 1
            
            else:
                rightPtr -= 1
                leftPtr += 1
        

        return ans
