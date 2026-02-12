class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        parenDict = {'(' : ')', '{' : '}', '[' : ']'}

        for paren in s:

            if paren in parenDict:

                stack.append(paren)

            else:

                if not stack:

                    return False
                
                else:

                    if parenDict[stack.pop()] != paren:

                        return False

        return not stack #if the stack is empty -> return true
