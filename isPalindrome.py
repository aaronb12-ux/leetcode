class Solution:
    def isPalindrome(self, s: str) -> bool:

        #inputs: the string (iterate over this)

        #output: boolean (true if palindrome, else false)

        '''
        remove all non alphanumeric chars and convert chars to lower

        check if string is palindrome

        '''

        if not s or len(s) == 0:
            return True

        alphanumString = ""

        for char in s:

            if char.isalnum():

                if char.isalpha():

                    alphanumString += char.lower()

                else:

                    alphanumString += char
        
        leftPtr = 0
        rightPtr = len(alphanumString) - 1

        while leftPtr <= rightPtr:

            if alphanumString[leftPtr] != alphanumString[rightPtr]:
                return False
            
            else:
                leftPtr += 1
                rightPtr -= 1
        

        return True
