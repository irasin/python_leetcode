"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 无脑做法
# 时间复杂度 O(nlogn) 空间复杂度O(1)
from typing import List
from random import randint
class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]


Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)

## 快速排序的利用
## 快速排序是重复将nums分成 [nums < pivot] pivot [nums >= pivot]的三部分
## 事实上，如果[nums >= pivot]的长度为k - 1，则pivot为第k大的元素
## 所以，我们可以参考快速排序，定义一个快速查找
## 对于给定的nums和idx，随机生成pivot,将pivot先pop,nums分成left = [nums < pivot] 和right = [nums >= pivot]的部分
## 如果len(right) == idx - 1,  return pivot
## 如果len(right) > idx - 1，对right部分快速查找idx - 1
## 如果len(right) < idx - 1，对left部分快速查找idx - 1 - len(right)

## 也可以使用推排序（需要学习下）

## 时间复杂度 O(n)(因为是随机选择pivot)，空间复杂度O(logn)(递归使用栈空间？)


import random

class Solution:
    def findKthLargest(self, nums, k):
        return self.quicksearch(nums, k)


    def quicksearch(self, nums, idx):
        if len(nums) == 0:
            return 
        p_idx = random.randint(0, len(nums) - 1)
        pivot = nums.pop(p_idx)
        
        right = [i for i in nums if i >= pivot]
        if len(right) == idx - 1:
            return pivot
        elif len(right) > idx - 1:
            return self.quicksearch(right, idx)
        else:
            left = [i for i in nums if i < pivot]
            return self.quicksearch(left,  idx - 1 - len(right))
   

Solution().findKthLargest([3, 2, 1, 5, 5,6,5,6, 4], 2)


# ## 这里顺便复习下quicksort的写法
# def quicksort(nums):
#     if len(nums) == 0:
#         return []
#     p_idx = random.randint(0, len(nums) - 1)
#     pivot = nums[p_idx]
#     left = [i for i in nums if i < pivot]
#     center = [i for i in nums if i == pivot]
#     right = [i for i in nums if i > pivot]


#     res = quicksort(left) + center + quicksort(right)
#     return res

