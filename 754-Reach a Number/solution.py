class Solution:
    def reachNumber(self, target: int) -> int:
        t = abs(target)
        min_n = int(math.ceil((-1 + math.sqrt(1+8*t)) / 2))
        while target%2 != (min_n*(min_n+1)//2)%2:
            min_n += 1
        return int(min_n)