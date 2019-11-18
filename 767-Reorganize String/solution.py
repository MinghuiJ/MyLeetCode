class Solution:
    def reorganizeString(self, S: str) -> str:
        import collections
        counter = collections.Counter(S)
        res = [0] * len(S)
        for i in range(len(S)):
            flag = False
            for k, v in counter.most_common():
                if v>=1 and k not in res[i-1:i]:
                    res[i] = k
                    counter[k] -= 1
                    flag = True
                    break
            if not flag:
                return ''
        return ''.join(res)