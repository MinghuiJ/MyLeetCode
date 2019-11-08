# Question
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5

Output: True

Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3

Output: False

# 想法
* 循环遍历找，最大到sqrt(c)，需要注意两个因子相等的情况。按此思路写出代码如下:

    ```python
    class Solution:
        def judgeSquareSum(self, c: int) -> bool:
            if c==0:
                return True
            import math
            n = int(math.sqrt(c))
            mp = []
            for i in range(n+1):
                squa = i*i
                if c-squa in mp or squa*2==c:
                    return True
                mp.append(squa)
            return False
    ```
    思路没有错，但在c很大的时候出现**Time Limit Exceeded**错误， = =。。。

<br/>

* 翻看评论区，找到一个双指针思路如下：

    ```python
    class Solution:
        def judgeSquareSum(self, c: int) -> bool:
            n = int(math.sqrt(c))
            left = 0
            right = n
            while left<=right:
                res = left**2 + right**2
                if  res<c:
                    left += 1
                elif res>c:
                    right -= 1
                else:
                    return True
            return False
    ```