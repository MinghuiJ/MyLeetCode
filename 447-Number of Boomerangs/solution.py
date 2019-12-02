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