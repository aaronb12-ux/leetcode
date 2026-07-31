class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        '''
            create a prefix sum!

            [4, 5, 2, 1] -> first sort
            [1, 2, 4, 5]

            [1, 3, 7, 12] target == query ==  10

            l = 0
            r = 3
             middle = 1

            l = 2
            r = 3
            middle = 2

            l = 3
            r = 3
            middle = 3


            '''

        nums.sort()
        prefixSum = [nums[0]]

        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])

        ans = []

        def binarySearch(query):
            left = 0
            right = len(prefixSum) - 1

            while left <= right:

                middle = (left + right) // 2

                if prefixSum[middle] == query:
                    return middle + 1
                
                elif prefixSum[middle] < query:
                    left = middle + 1
                
                else:
                    right = middle - 1
            
            return left
                
        for query in queries:
            ans.append(binarySearch(query))
        
        return ans
