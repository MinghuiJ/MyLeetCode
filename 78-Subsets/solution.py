class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        subset = []
        self.bfs(nums, 0, subset, ret)
        return ret
    
    def bfs(self, nums, index, subset, ret):
        # use list() to achieve deep copy here 
        ret.append(list(subset))
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.bfs(nums, i+1, subset, ret)
            subset.pop()