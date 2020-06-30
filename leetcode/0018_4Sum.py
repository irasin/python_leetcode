

"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## 暴力穷举
## O(N^4)，不写了，意义不大

## 双指针
## 首先排序
## 设置四个指针，i, j固定从左到右遍历，k = j + 1, l = size - 1双指针移动即可
## 实现上大抵和三数之和没有差别，注意剪枝和去重即可
## 在去重时特别需要注意一个边界问题，k < l是不是需要？
## 答案是需要的，
## [1, 2, 3, 3, 3, 3] 如果是这样以恶搞数组，不加边界条件就会index out of range

## 时间复杂度 O(N^3)，空间复杂度 O(1)


class Solution:
    def fourSum(self, nums, target):
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: # 去重
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 去重
                    continue
                
                k = j + 1
                if nums[i] + nums[j] + nums[k] + nums[k + 1] > target: # 剪枝
                    break
                
                l = n - 1
                if nums[i] + nums[j] + nums[l - 1] + nums[l] < target: # 剪枝
                    continue
                
                while k < l:
                    sums = nums[i] + nums[j] + nums[k] + nums[l]
                    if sums == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:  # 去重
                            k += 1
                        l -= 1
                        while k < l and nums[l] == nums[l + 1]:  # 去重
                            l -= 1
                    elif sums > target:
                        l -= 1
                        while k < l and nums[l] == nums[l + 1]:  # 去重
                            l -= 1
                        
                    else:
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:  # 去重
                            k += 1
        return res
                        


Solution().fourSum([1, 0, -1, 0, -2, 2], 1)
Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)        
                        
