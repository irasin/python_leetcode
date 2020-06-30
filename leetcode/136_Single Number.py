"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


## 由于不能使用额外的空间，所以这里采取异或运算（XOR）
## 异或运算满足
##      a XOR a = 0 
##      a XOR 0 = a
##      结合律与交换律（可通过真伪表判断）

##  因此，对nums里所有元素做异或，出现两次的会变为0，出现一次的最终留下

## 时间复杂度 O(n)，空间复杂度O(1)
class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res = res ^ i
        return res
  
Solution().singleNumber([4,1,2,1,2])


## 这里补充一个有趣的算法，虽然用到了set导致不合要求
# class Solution:
#     def singleNumber(self, nums):
#         res = sum(set(nums)) * 2 - sum(nums)
#         return res


# Solution().singleNumber([4, 1, 2, 1, 2])
