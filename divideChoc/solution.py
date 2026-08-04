class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        if len(sweetness) == k + 1:
            return min(sweetness)

        def isValidSweetness(middle):

            cutsMade = 0
            currCutSweetness = 0

            for piece in sweetness:
                currCutSweetness = currCutSweetness + piece

                if currCutSweetness >= middle:
                
                    cutsMade += 1
                    currCutSweetness = 0
            
         
            return cutsMade >= k + 1

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)
        best = 0
        while left <= right:

            middle = (left + right) // 2

            if isValidSweetness(middle):
                best = middle
                left = middle + 1
            else:
                right = middle - 1
        
        return best


