class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dp(i):

            if i == 0:
                return 0
            if i == 1:
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

            return memo[i]

        memo = {}
        return dp(len(cost))


'''
States: index of current step -> dp(i) returns the minimum cost from start to the ith step

Recurrence Relation: from the current step, we could have gotten here from one step below or two steps below. Let's say i == 50 and we are on the 50th step. To get here, it would have taken the minimum cost to get to the 49th step, plus the cost of the 49th step. Or the minimum cost of the 48th step, plus the cost of the 48th step. More generally: dp(i) = min(dp(i - 1) + cost(i - 1), dp(i - 2) + cost(i - 2))

Base Case: We can start at step 0 or 1, so dp(0) = dp(1) = 0. This is because it costs 0 to start here. We only once we make a first turn from these spots.
'''
        
