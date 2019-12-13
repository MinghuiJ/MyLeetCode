# Question
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

**Example:**

    Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
    Output: [3,3,5,5,6,7] 
    Explanation: 

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1  [3  -1  -3] 5  3  6  7       3
    1   3 [-1  -3  5] 3  6  7       5
    1   3  -1 [-3  5  3] 6  7       5
    1   3  -1  -3 [5  3  6] 7       6
    1   3  -1  -3  5 [3  6  7]      7

**Note:**
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

**Follow up:**
Could you solve it in linear time?

# 想法

* 第一想法是用优先队列，但每次滑动的时候需要维护一个最大堆，总体复杂度为`O(nlogn)`，不是线性时间复杂度
* 考虑双向队列（存放元素的索引），每当有滑动到下一个位置，查看新的元素是否大于等于队列头索引对应的元素，如果是，则将队列所有东西全部`pop`并将其索引加入队列，否则直接加入到列尾。这样队列的头部始终是当前窗口中最大元素的索引，将其加入结果`list`中即可

    ```python
    class Solution:
        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            if len(nums)<k or k<=0:
                return []
            window_index, res = [], []
            for i in range(len(nums)):
                if i>=k and window_index[0] <= i - k:
                    window_index.pop(0)
                while window_index and nums[window_index[-1]] <= nums[i]:
                    window_index.pop()
                window_index.append(i)
                if i>=k-1:
                    res.append(nums[window_index[0]])
            return res
    ```