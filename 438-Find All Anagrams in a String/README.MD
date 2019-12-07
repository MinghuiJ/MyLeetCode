# Question

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

**Example 1:**

    Input:
    s: "cbaebabacd" p: "abc"

    Output:
    [0, 6]

    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

**Example 2:**

    Input:
    s: "abab" p: "ab"

    Output:
    [0, 1, 2]

    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".

# 想法

* 第一想法对p进行排序，然后遍历s，每次对s中len(p)个字符进行排序，如果跟p排序后一样，则遍历的起始位置加入到结果list中。很显然，TLE

* 后来想到使用一个数字来代表p中每个字符，然后计算字符串的总和，这样只要比较和就可以，不需要排序，但是自己没有想到用哪些数字代表一个字符才能使得不同的和代表不同的字符串。看到讨论区，发现想法想到了，就是没有想到实现的方法，原来用hash就行

```python
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
```