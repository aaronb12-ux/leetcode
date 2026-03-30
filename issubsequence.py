class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        '''
            inputs: 
                s -> checking if it is a subsequence in t
                t -> string we are checking if s is a subsequence in

            outputs:
                boolean: whether s in a subsequence in t

            
            algorithm:
                two pointers: 
        '''

        if not s:
            return True

        sPtr = 0

        for char in t:
            if s[sPtr] == char:
                sPtr += 1
            
            if sPtr == len(s):
                return True
            
        return False
