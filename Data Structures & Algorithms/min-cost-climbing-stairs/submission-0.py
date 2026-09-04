class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mc = [cost[0],cost[1]]

        for i in range(2,len(cost)):
            subproblem = cost[i] + min(mc[i-1],mc[i-2])
            mc.append(subproblem)
        return min(mc[-1],mc[-2])

        