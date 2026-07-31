class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        '''
            sort nums
            [1, 2, 4, 5]
        '''

        ans = []

        def solveQuery(query, sortedNums):
            currTotal = 0
            count = 0
            
            for num in sorted(sortedNums):

                if currTotal + num > query:
                    return count
                else:
                    currTotal += num
                    count += 1
            
            return count

        sortedNums = sorted(nums) 
        for num in queries:
            maxSize = solveQuery(num, sortedNums)
            ans.append(maxSize)

        return ans
