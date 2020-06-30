"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

 

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
 

提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## 考虑到复杂度要求，不能使用set/dict，也不能双重循环
## 否则我们可以用一个set轻松解决问题


# class Solution:
#     def firstMissingPositive(self, nums):
#         candidate = set(range(1, len(nums) + 1))
#         return min(candidate - set(nums))

# Solution().firstMissingPositive([1, 2, 0])
# Solution().firstMissingPositive([3, 4, -1, 1])


## 在这种情况下，我们使用一种所谓原地哈希的操作
## 即，让数组记录额外的信息
## 本来，数组中的index和对应的值是没有关联的
## 这里，我们映射一种关系，使得，nums[index]  -> index + 1 == value

## 为什么可以这样做呢
## 我们考虑题目要求，N为数组长度时，满足条件的正整数一定在1到N+1之间
## 因此我们只需原数组中，各个1到N的value都放在的对应下表为index = value - 1的位置即可，
## 如 [3, 4, -1, 1] -> [1, -1, 3, 4]
## 这个时候，第一个不满足nums[index] == index + 1的地方，index + 1就是缺失的正整数

## 所以我们需要做的是，遍历每一个index，使得该index处的值在其该在的地方
## 然后遍历调整后的数组，找到缺失的数
## 时间复杂度O(n)，空间复杂度O(1) 

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            # 当nums[i]在1到n之间，且nums[i]的值应该对应的index不为nums[i] - 1时调整
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 将nums[i]的值放到index为nums[i] - 1处
                # 将nums[i] - 1的值放到index为i处
                
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
                ## 注意
                ## 此处不能写成下面的样子
                ## nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                ## 原因：
                ## 执行 a, b = b, a时，
                ## 是按 tmp = a, a = b, b = tmp的顺序
                ## 如果按上述写法，先把nums[nums[i] - 1]的值赋值给 nums[i],
                ## 再把nums[i]的值赋值给nums[nums[i] - 1],
                ## 此时注意nums[i] - 1这个index里的nums[i]已经是更新过了的
                ## 所以此时执行nums[nums[i] - 1] = nums[i]，就不是预期的结果了
                ## 出现这个问题的原因很简单，因为交换i和nums[i] - 1的值时，nums[i]会变化
                ## 所以交换的index会变化
                
                ## 而nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]是不会有问题的
                ## 因为，先把nums[i]的值赋给nums[nums[i] - 1]
                ## 再把nums[nums[i] - 1]的值赋值给nums[i]
                ## 在进行完第一步时，nums[i]本身没有变，所以不会出现错误
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1   
        return n + 1 

Solution().firstMissingPositive([1, 2, 0])
Solution().firstMissingPositive([3, 4, -1, 1])

## 为了避免上述的错误，我们可以显性地指定交换的index，确保交换时它们不变


class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            # 当nums[i]在1到n之间，且nums[i]的值应该对应的index不为nums[i] - 1时调整
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                idx1 = i
                idx2 = nums[i] - 1
                # 通过固定idx1, idx2的值，就不会发生交换时index变化的问题了
                self.swap(nums, idx1, idx2)

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
            
    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]


Solution().firstMissingPositive([1, 2, 0])
Solution().firstMissingPositive([3, 4, -1, 1])
