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