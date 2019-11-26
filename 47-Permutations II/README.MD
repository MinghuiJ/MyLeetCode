# Question

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

**Example:**

    Input: [1,1,2]
    Output:
    [
        [1,1,2],
        [1,2,1],
        [2,1,1]
    ]

# 想法
* BFS预定，跟subsets有相似之处，只不过需要考虑有重复元素，且最终结果只需要搜索中路径元素个数等于给定数组元素个数的路径。

    ```python
    class Solution:
        def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            res, visited = [], [False] * len(nums)
            subset = []
            nums.sort()
            self.bfs(nums, subset, visited, res)
            return res
            
        def bfs(self, nums, subset, visited, res):
            if len(subset)==len(nums):
                res.append(subset)
                return
            for i in range(len(nums)):
                if not visited[i]:
                    if i>0 and not visited[i-1] and nums[i]==nums[i-1]:
                        continue
                    visited[i] = True
                    self.bfs(nums, subset+[nums[i]], visited, res)
                    visited[i] = False
    ```