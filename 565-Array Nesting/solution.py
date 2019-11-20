class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            if nums[i]==-1:
                continue
            length, idx = 0, i
            while nums[idx] != -1:
                nums[idx], idx = -1, nums[idx]
                length += 1
            if res < length:
                res = length
        return res