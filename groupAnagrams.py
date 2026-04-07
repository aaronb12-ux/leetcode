from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
                inputs:
                    strs: array of strings
                output:
                    an array of arrays, where in each subarray there are similar anagrams

        data structures:
            hashmap for sorted lookups
        Time Complexity:
            O(n * klogk)

            n is length of array, k is length of longest string
        '''

        hashmap = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))

            hashmap[sortedS].append(s)
        

        groupedAnagrams = list(hashmap.values())

        return groupedAnagrams
