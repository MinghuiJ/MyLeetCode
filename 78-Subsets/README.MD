# Question
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

# 想法
* 起初自己没想到递归，看了讨论区之后，看到一个递归解法，其中使用了两个list作为递归函数的参数。一个是当前子集list，一个是最终结果list，由于当前子集list在递归不同层次中不一样，因此该list需要进行深拷贝（deep copy）。程序中直接使用一个强制list转换进行deep copy，开始没有想到这一层，直接把list名进行传递，最终得到的是空集合。这是一个大坑。而最终结果list需要一直进行append，结果放到这同一个list中，因此不需要进行deep copy。