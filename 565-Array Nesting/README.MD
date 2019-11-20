# Question

A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

 

**Example 1:**

    Input: A = [5,4,0,3,1,6,2]
    Output: 4
    Explanation: 
    A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

    One of the longest S[K]:
    S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
 

**Note:**

    1. N is an integer within the range [1, 20,000].
    2. The elements of A are all distinct.
    3. Each element of A is an integer within the range [0, N-1].

# 想法
* 写了几版都TLE，原因在于复杂度写成了O(n <sup>2</sup> )，实际上O(n)就够了，直接在原始数据上改成一个不可能出现的数字作为是否遍历过的标志位即可。

    ```python
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
    ```