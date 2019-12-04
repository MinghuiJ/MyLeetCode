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