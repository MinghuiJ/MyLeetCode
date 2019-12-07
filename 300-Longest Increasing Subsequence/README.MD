# Question

Given an unsorted array of integers, find the length of longest increasing subsequence.

**Example:**

    Input: [10,9,2,5,3,7,101,18]
    Output: 4 
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

**Note:**

* There may be more than one LIS combination, it is only necessary for you to return the length.
* Your algorithm should run in O(n2) complexity.

**Follow up:** Could you improve it to O(n log n) time complexity?

# 想法

* 经典dp问题，遍历数组`(i)`，然后在`(0, i)`之间再遍历`(j)`，如果`nums[i]>nums[j]`,则`dp[i] = max(dp[i], dp[j]+1)`

* 优化方法看到一个老哥优化到`O(n)`，具体是维护一个上升数组`asc`。遍历`nums`数组，如果`nums[i]>asc[-1]`，则把`nums[i]`加入到`asc`中，否则使用二分查找寻找`nums[i]`应该被插入到`asc`的哪个位置上`j`（该步骤使用bisect库，学到了），然后`asc[j]=nums[i]`，即取代原来的位置元素，最后返回`len(asc)`即可。自己理解了一下，发现`asc`在维护过程中以尽可能小的元素替代大的元素，这样让上升空间更大，在后续即拥有更长的上升序列，同时在替换的那一时刻保持了上升序列元素个数的不变

* **优化前**

    ```python
    class Solution:
        def lengthOfLIS(self, nums: List[int]) -> int:
            if len(nums)==0:
                return 0
            dp = [1] * len(nums)
            for i in range(1, len(nums)):
                for j in range(0, i+1):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j]+1)
            
            return max(dp)
    ```

* **优化后**

    ```python
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
    ```