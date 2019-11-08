class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_costs = sorted(costs, key=lambda x:x[0]-x[1])
        n = len(sorted_costs) // 2
        res = 0
        for i in range(n):
            res += sorted_costs[i][0]
        for i in range(n, len(sorted_costs)):
            res += sorted_costs[i][1]
        return res