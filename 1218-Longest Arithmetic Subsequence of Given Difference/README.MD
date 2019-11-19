# Question
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

 

**Example 1:**

    Input: arr = [1,2,3,4], difference = 1
    Output: 4
    Explanation: The longest arithmetic subsequence is [1,2,3,4].

**Example 2:**

    Input: arr = [1,3,5,7], difference = 1
    Output: 1
    Explanation: The longest arithmetic subsequence is any single element.

**Example 3:**

    Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
    Output: 4
    Explanation: The longest arithmetic subsequence is [7,5,3,1].
 

**Constraints:**

* 1 <= arr.length <= 10^5
* -10^4 <= arr[i], difference <= 10^4

# 想法
* dpdpdpdp，自己写的很麻烦，评论区四行代码如下
* 利用collections.Counter()，需要注意的是这个类似字典的结构，对于不存在的键，其值为0，这点倒是方便，不需要再去判断是否存在在Counter中

    ```python
    class Solution:
        def longestSubsequence(self, arr: List[int], difference: int) -> int:
            import collections
            dp = collections.Counter()
            for num in arr:
                dp[num] = max(dp[num], dp[num - difference] + 1)
            return max(dp.values())
    ```