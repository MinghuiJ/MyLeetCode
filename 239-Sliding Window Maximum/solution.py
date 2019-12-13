class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) < k or k <= 0:
            return []
        window_index, res = [], []
        for i in range(len(nums)):
            if i >= k and window_index[0] <= i - k:
                window_index.pop(0)
            while window_index and nums[window_index[-1]] <= nums[i]:
                window_index.pop()
            window_index.append(i)
            if i >= k-1:
                res.append(nums[window_index[0]])
        return res
