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