class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        if len(nums)==0:
            return 0
        asc = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > asc[-1]:
                asc.append(nums[i])
            else:
                insert_loc = bisect.bisect_left(asc, nums[i])
                asc[insert_loc] = nums[i]
        return len(asc)