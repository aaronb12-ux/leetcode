class Solution:
    def fib(self, n: int) -> int:

        def dp(i):

            if i == 0:
                return 0
            
            if i == 1:
                return 1
            
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i - 1) + dp(i - 2)

            return memo[i]
        
        memo = {}
        return dp(n)






'''
states: current number 'n'

recurrance relation: dp(i) = dp(i - 1) + dp (i - 2)

base case: dp(0) == 0 and dp(1) == 1

'''
