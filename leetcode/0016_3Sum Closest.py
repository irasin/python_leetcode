"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1, 2, 1, -4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1=2) 。
 

提示：

3 <= nums.length <= 10 ^ 3
-10 ^ 3 <= nums[i] <= 10 ^ 3
-10 ^ 4 <= target <= 10 ^ 4

来源：力扣（LeetCode）
链接：https: // leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## 暴力穷举
## 时间复杂度O(n^3)，所以绝对会超时
class Solution:
    def threeSumClosest(self, nums, target):
        res = float('inf') 
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == target:
                        return target
                    if abs(nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
        return res
        
Solution().threeSumClosest([-1, 2, 1, -4], 1)
Solution().threeSumClosest([-1, 1,3, 2,1, -4], 5)

## 双指针（外部for循环，内部while循环）
## 和第15题类似，但判定条件不同，需要注意
## 作为优化部分，去重剪枝都是可以添加的

class Solution:
    def threeSumClosest(self, nums, target):
        res = float('inf') # 初始化res为无限大
        n = len(nums)
        nums.sort()
        
        for i in range(n - 2): # 遍历i
            if i > 0 and nums[i] == nums[i - 1]: #  去重
                continue
            
            j = i + 1
            k = n - 1
            
            if nums[i] + nums[j] + nums[k] == target: # 相等的话直接return即可
                return target
            
            if nums[i] + nums[j] + nums[j + 1] > target: # 剪枝
                if abs(nums[i] + nums[j] + nums[j + 1] - target) < abs(res - target):
                    res = nums[i] + nums[j] + nums[j + 1]
                break
            
            
            if nums[i] + nums[k - 1] + nums[k] < target: # 剪枝
                if abs(nums[i] + nums[k - 1] + nums[k] - target) < abs(res - target):
                    res = nums[i] + nums[k - 1] + nums[k]
                continue
                
            while j < k: # 内部双指针用while
                sums = nums[i] + nums[j] + nums[k]
                if abs(sums - target) < abs(res - target): # 判断是否需要更新
                    res = sums
                    
                if sums == target: #相等直接return
                    return sums
                
                elif sums > target: #sums > target，需要把k向左移动
                    k -= 1 
                    while j < k and nums[k] == nums[k + 1]: # 去重
                        k -= 1
                else: # sums < target，需要把j向右移动
                    j += 1
                    while j < k and nums[j] == nums[j - 1]: # 去重
                        j += 1
        
        return res


Solution().threeSumClosest([-1, 2, 1, -4], 1)
Solution().threeSumClosest([-1, 1, 3, 2, 1, -4], 5)
