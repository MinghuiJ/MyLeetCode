# Question
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: \[[10,20],[30,200],[400,50],[30,20]]

Output: 110

Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100

It is guaranteed that costs.length is even.

1 <= costs[i][0], costs[i][1] <= 1000

# 想法
* 开始思路想到排序，而且可能用到贪心，但不知按什么排序，想了半天也没想出来，太菜了。最后还是看评论区，直接按两个城市的代价差排序。。。我太菜了

    ```python
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
    ```