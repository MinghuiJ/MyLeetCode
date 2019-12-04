# Question
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
What is the largest possible number of moves we can make?

 

**Example 1:**

    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5

**Example 2:**

    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3

**Example 3:**

    Input: stones = [[0,0]]
    Output: 0
 

**Note:**

    1 <= stones.length <= 1000
    0 <= stones[i][j] < 10000

# 想法

* dfs搞起来，建立节点（每个点为一个节点）邻接表（两个点之间`x`或`y`相同，则两个点邻接），之后深度搜索，每当遇到一个新的节点，则说明此节点可以进行move，最终结果加1。

```python
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        l = len(stones)
        self.visit = [False] * l
        self.ret = 0
        
        def dfs(i):
            for node in graph[i]:
                if not self.visit[node]:
                    self.ret += 1
                    self.visit[node] = True
                    dfs(node)
        
        graph = {}
        for i in range(l):
            for j in range(i+1, l):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    if i in graph:
                        graph[i].append(j)
                    else:
                        graph[i] = [j]
                    if j in graph:
                        graph[j].append(i)
                    else:
                        graph[j] = [i]
        
        for i in graph:
            if not self.visit[i]:
                self.visit[i] = True
                dfs(i)
        
        return self.ret
```