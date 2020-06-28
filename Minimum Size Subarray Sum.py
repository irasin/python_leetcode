## 暴力穷举：从每个index开始，计算累加和达到s时所需的长度，返回其中的最小值
## 时间复杂度 O(n^2)，空间复杂度 O(1)
class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums) # 获取数组长度
        res = n + 1 # res初始化为数组长度加1
        
        for i in range(n): 
            # i = 0 开始遍历到n
            total = 0 # 从i = 0开始的累加和初始化为0
            for j in range(i, n): 
                # j = i 开始遍历到n
                total += nums[j] # 获取i到j的累加和
                if total >= s:
                    # 如果累加和大于或等于s，停止遍历，更新最小长度
                    res = min(res, j - i + 1) # 更新子数组最短长度，注意i到j之间的数为 j - i + 1
                    break 
        # 如果res == n + 1，说明sum(nums) < s，输出0，否则输出res
        return 0 if res == n + 1 else res 


Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
Solution().minSubArrayLen(4, [1, 4, 4])
Solution().minSubArrayLen(15, [1, 2, 3, 4, 5])

## 前n项和加二分搜索: 构建额外的数组sums， 储存nums里的前n项和
## 即sums = [0, nums[0], nums[0] + nums[1],...]
## 此时sums[i]表示nums的前i项的和，注意sums[0]等于0，这个很重要
## 然后从sums中，通过二分搜索找到最小的bound(bound>=i)，使得sums[bound] - sums[i - 1] >= s
## 此时判断子数组长度bound - i + 1 是否比res短
import bisect
## bisect提供通过二分搜索找到该插入的index的函数 
## bisect.bisect_left与bisect.bisect(等价于bisect.bisect_right)
## 其中bisect_left是将相同的值插入到原值的左边
## example:
# a = [1, 2, 4, 6]
# bisect.bisect(a, 3) # 2
# bisect.bisect(a, 4) # 3
# bisect.bisect_left(a, 3) # 2
# bisect.bisect_left(a, 4) # 2


## 时间复杂度为O(nlogn)，空间复杂度为O(n)
  
#  -------------------------------------------------------------------------------------------------
  
class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums) # 获取数组长度
        res = n + 1 # res初始化为数组长度加1
        
        sums = [0] #初始化sums，第一个元素为0，表示nums的前0项和
        for i in nums: # 添加nums的前i项和到sums中，注意最终len(sums) = n + 1
            sums.append(sums[-1] + i)
        
        for i in range(1, n + 1): # 从i = 1到 n进行遍历
            target = sums[i - 1] + s # 计算 target = sums[i - 1] + s的值
            idx = bisect.bisect_left(sums, target) # 通过二分搜索查找target应该被插到第几位
            if idx <= n: # 如果idx = n + 1，说明target会被插到sums的最右边，即sums[i - 1] + s大于sums[-1]
                res = min(res, idx - i + 1) # 更新子数组最短长度，注意i到j之间的数为 j - i + 1
        
        # 如果res == n + 1，说明sum(nums) < s，输出0，否则输出res
        return 0 if res == n + 1 else res


Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
Solution().minSubArrayLen(4, [1, 4, 4])
Solution().minSubArrayLen(15, [1, 2, 3, 4, 5])


# ###  这里作为补充，自己实现二分搜索
# def has_element(l, target):
#     exist = False
#     low, high = 0, len(l)
#     while low < high:
#         # print(low, high)
#         mid = (low + high) // 2
#         if l[mid] == target:
#             return True
#         elif l[mid] > target:
#             high = mid
#         else:
#             low = mid + 1
#     return False 

# has_element([1, 2, 4, 6, 7], 2)
   

# ## 自己实现bisect
# ## left和right的区别在于，target是否包含在左边界中
# def binary_search_left(l, target):
#     low, high = 0, len(l)
#     while low < high:
#         mid = (low + high) // 2
#         if l[mid] < target:
#             low = mid + 1
#         else:
#             high = mid
#     return high


# def binary_search_right(l, target):
#     low, high = 0, len(l)
#     while low < high:
#         mid = (low + high) // 2
#         if l[mid] <= target:
#             low = mid + 1
#         else:
#             high = mid
            
#     return high

# a = [1, 2, 4, 6]
# binary_search_left(a, 4)
# binary_search_right(a, 4)

#  -------------------------------------------------------------------------------------------------

## 通过双指针的方式求解
## 设定i，j都从0开始，向右移动j，先找到满足i到j之间的数字和total为s以上的窗口，判断是否要更新res，
## 然后使i += 1，total减去nums[i]，此时数字和应该小于s了，需要继续向右移动j，重复上述操作
## 直至j移动到n

## 时间复杂度 O(n)，空间复杂度O(1)
class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums) # 获取数组长度
        res = n + 1 # res初始化为数组长度加1
        i, j = 0, 0 # i, j初始化为0, 0
        total = 0 # 窗口累加和初始化为0
        while j < n: # j没有达到nums末尾时遍历
            total += nums[j] # total加上nums[j]
            while total >= s: # 当total >= s时，更新子数组长度，向右移动i并修改total的值
                res = min(res, j - i + 1) # 更新子数组最短长度，注意i到j之间的数为 j - i + 1
                # total减去i对应的值nums[i]，并向右移动1
                total -= nums[i]
                i += 1

            j += 1 # 向右移动j
        # 如果res == n + 1，说明sum(nums) < s，输出0，否则输出res
        return 0 if res == n + 1 else res


Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
Solution().minSubArrayLen(4, [1, 4, 4])
Solution().minSubArrayLen(15, [1, 2, 3, 4, 5])
