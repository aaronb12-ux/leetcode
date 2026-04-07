from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
                inputs:
                    nums: list of integers
                    k: need to return the k most frequent elements
        '''

        counts = defaultdict(int)


        for num in nums:

            counts[num] += 1
            
        
        #sort the keys in the dictionary from greatest to least and get a list of the keys
        sortedDict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        keys = list(sortedDict.keys())

        
        ans = []

        for i in range(k):
            ans.append(keys[i])
        
        return ans
