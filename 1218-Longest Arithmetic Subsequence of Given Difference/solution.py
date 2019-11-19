class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        import collections
        dp = collections.Counter()
        for num in arr:
            dp[num] = max(dp[num], dp[num - difference] + 1)
        return max(dp.values())