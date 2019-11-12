# Question

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

**Example 1:**

    Input: target = 3
    Output: 2
    Explanation:
    On the first move we step from 0 to 1.
    On the second step we step from 1 to 3.

**Example 2:**

    Input: target = 2
    Output: 3
    Explanation:
    On the first move we step from 0 to 1.
    On the second move we step  from 1 to -1.
    On the third move we step from -1 to 2.

**Note:**

    target will be a non-zero integer in the range [-10^9, 10^9].

# 想法

* 又是没有头绪的一道easy题，看了讨论区发现是道数学题，，，我太南了
* 首先target的正负号不影响结果，直接abs，然后分析为正数的时候。先假设1,2...,n都向右移动，则等差数列求和，n(n+1)/2，令其等于target，则求解一个二元一次方程，取其正解，向上取整（向下的话即使全部向右也还是达不到target），记为min_n。然后对min_n分析，若1,2...,min_n的和sum与target同奇或同偶，则只需要将(sum-target)/2的那一步向左走即可，因此总步数为min_n；如果奇偶性不同，则min_n+1，计算sum，比较奇偶，重复以上步骤直到sum与target奇偶性相同。

    ```python
    class Solution:
        def reachNumber(self, target: int) -> int:
            t = abs(target)
            min_n = int(math.ceil((-1 + math.sqrt(1+8*t)) / 2))
            while target%2 != (min_n*(min_n+1)//2)%2:
                min_n += 1
            return int(min_n)
    ```