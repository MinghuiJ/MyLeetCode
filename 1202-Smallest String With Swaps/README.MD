# Question
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 
**Example 1:**

    Input: s = "dcab", pairs = [[0,3],[1,2]]
    Output: "bacd"
    Explaination: 
    Swap s[0] and s[3], s = "bcad"
    Swap s[1] and s[2], s = "bacd"

**Example 2:**

    Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
    Output: "abcd"
    Explaination: 
    Swap s[0] and s[3], s = "bcad"
    Swap s[0] and s[2], s = "acbd"
    Swap s[1] and s[2], s = "abcd"

**Example 3:**

    Input: s = "cba", pairs = [[0,1],[1,2]]
    Output: "abc"
    Explaination: 
    Swap s[0] and s[1], s = "bca"
    Swap s[1] and s[2], s = "bac"
    Swap s[0] and s[1], s = "abc"
 
**Constraints:**

* 1 <= s.length <= 10^5
* 0 <= pairs.length <= 10^5
* 0 <= pairs[i][0], pairs[i][1] < s.length
* s only contains lower case English letters.

# 想法
* 自己的想法是合并所有可以合并的项（合并后所有位置的字母都可以互换），然后合并后的位置对应字母进行排序即可。但在测试用例33的时候Time Limit Exceeded，循环太复杂了
* 评论区答案：建立连通图，BFS搜一下，产生的每一条路径上的所有字符都是可以互换的，因此只需要对同一路径上对应的字母进行排序然后放在指定的位置即可

    ```python
    class Solution:
        def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
            graph = {}
            for node in range(len(s)):
                graph[node] = []
            for u,v in pairs:
                graph[u].append(v)
                graph[v].append(u)
            
            position = {}
            for node in range(len(s)):
                if node not in position:
                    idx = set()
                    self.dfs(node, idx, graph)
                    self.assign_each_char(s, idx, position)
            res = ''
            for i in range(len(s)):
                res += position[i]
            return res
            
        def assign_each_char(self, s, idx, position):
            list_idx = sorted(list(idx))
            list_char = sorted([s[p] for p in list_idx])
            for i in range(len(list_idx)):
                position[list_idx[i]] = list_char[i]
            
        def dfs(self, node, idx, graph):
            idx.add(node)
            for item in graph[node]:
                if item not in idx:
                    self.dfs(item, idx, graph)
    ```