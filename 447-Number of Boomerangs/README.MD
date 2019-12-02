# Question

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

**Example:**

    Input:
    [[0,0],[1,0],[2,0]]

    Output:
    2

    Explanation:
    The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

# 想法
* 建立一个距离二维数组，`dist[i][j]`表示点`i`和点`j`之间的距离，之后对于`dist`数组每一行统计每个距离出现的次数`n`，由于点的顺序不同也计入最后结果，因此需要对组合数乘2，则共可组成如下数目的boomerang： $$C_n^2*2=n(n-1)$$ 然后把每一行的结果进行相加即可

    ```python
    class Solution:
        def numberOfBoomerangs(self, points: List[List[int]]) -> int:
            l = len(points)
            dist = [[0] * l for i in range(l)]
            res = 0
            for i in range(l):
                counter = {}
                for j in range(l):
                    if j > i:
                        dist[j][i] = dist[i][j] = (points[j][0]-points[i][0])**2 + (points[j][1]-points[i][1])**2
                    counter[dist[i][j]] = counter[dist[i][j]] + 1 if dist[i][j] in counter else 1
                res += sum(n * (n-1) for n in counter.values())
            return res
    ```
