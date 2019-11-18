# Question
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

**Example 1:**

    Input: S = "aab"
    Output: "aba"

**Example 2:**

    Input: S = "aaab"
    Output: ""

**Note:**

* S will consist of lowercase letters and have length in range [1, 500].

# 想法

* 建立每个字符及其出现次数的字典，然后从most_common遍历即可，每个字符若在其前一个位置和当前位置未出现过，则当前字符可以分配到当前位置。

    ```python
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
    ```