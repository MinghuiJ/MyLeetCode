# Question
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

**Example 1:**

    Input: 12
    Output: 21
 

**Example 2:**

    Input: 21
    Output: -1

# 想法

* 从低位往高位依次找比低位小的数字，并记录其位置，循环完成后，将记录位置中最靠近个位的数字 list_str_n[res[1]] 与其对应的那个低位 list_str_n[res[0]] 进行互换，然后再将 res[1] 往后的数字进行从小到大排序即可。

* 需要注意的一点是32位整数表示范围为 -2<sup>31</sup> ~ 2<sup>31</sup>-1

    ```python
    class Solution:
        def nextGreaterElement(self, n: int) -> int:
            n_str = str(n)
            list_str_n = [n_str[i] for i in range(len(n_str))]
            res = [len(list_str_n)-1, -1]
            for i in range(len(list_str_n)-1, 0, -1):
                for j in range(i-1, -1, -1):
                    if list_str_n[j]<list_str_n[i] and j>res[1]:
                        res = [i, j]
                        break
                if i<=res[1]:
                    break
            if res[1]==-1:
                return -1
            else:
                list_str_n[res[0]], list_str_n[res[1]] = list_str_n[res[1]], list_str_n[res[0]]
                right = sorted(list_str_n[res[1]+1:])
                ret_num = int(''.join(list_str_n[:res[1]+1]) + ''.join(right))
                if ret_num > (2**31-1):
                    return -1
                else:
                    return ret_num
    ```