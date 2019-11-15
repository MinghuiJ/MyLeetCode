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