class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dix={}
        def recursion(i):
            if i==0:
                return cost[0]
            if i==1:
                return cost[1]

            if i in dix:
                return dix[i]
            dix[i]=cost[i]+ min(recursion(i-1),recursion(i-2))


            return dix[i]

        return min(recursion(n-1),recursion(n-2))
        