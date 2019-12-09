# Question
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![avatar](robot_maze.png)
<font size="2">An obstacle and empty space is marked as `1` and `0` respectively in the grid.</font>

**Note:** *m* and *n* will be at most 100.

**Example 1:**

    Input:
    [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    Output: 2

    Explanation:
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

# 想法
* 62题的进阶题目，部分地方加了障碍，很容易理解，加了障碍的地方不可达，因此若`obstacleGrid[i][j]`是障碍，则将`dp[i][j]`置为0即可,其余同62题，`dp[i][j] = dp[i-1][j] + dp[i][j-1]`

    ```python
    class Solution:
        def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
            n = len(obstacleGrid)
            m = len(obstacleGrid[0])
            dp = [[0]*(m+1) for i in range(n+1)]
            dp[0][1] = 1
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if obstacleGrid[i-1][j-1]==1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[n][m]
    ```