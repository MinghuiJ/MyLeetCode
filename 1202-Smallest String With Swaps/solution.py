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
            position[list_idx[i]]=list_char[i]
        
    def dfs(self, node, idx, graph):
        idx.add(node)
        for item in graph[node]:
            if item not in idx:
                self.dfs(item, idx, graph)