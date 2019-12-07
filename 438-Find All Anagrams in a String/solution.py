class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        s_hash, p_hash = 0, 0
        ret = []
        if p_len > s_len:
            return []
        for i in range(p_len):
            s_hash, p_hash = s_hash + hash(s[i]), p_hash + hash(p[i])
        if s_hash == p_hash:
            ret.append(0)
        for i in range(p_len, s_len):
            s_hash += hash(s[i]) - hash(s[i-p_len])
            if s_hash == p_hash:
                ret.append(i - p_len + 1)
        return ret