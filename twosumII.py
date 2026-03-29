class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        '''
        inputs: 
            numbers: array of ints (starts at index 1)
            target: target sum 
        
        output:
            pair of nums that sum to the target
        '''

        ans = []
        leftPtr = 0
        rightPtr = len(numbers) - 1

        while leftPtr <= rightPtr:

            currentSum = numbers[leftPtr] + numbers[rightPtr]

            if currentSum == target:
  
                return [leftPtr + 1, rightPtr + 1]
            
            elif currentSum > target:
                rightPtr -= 1
            
            else:
                leftPtr += 1
        
        return ans
        
