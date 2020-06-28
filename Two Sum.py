"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

## 暴力穷举
## 时间复杂度 O(n^2)，空间复杂度O(1)
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return[i, j]
                
Solution().twoSum([2, 7, 11, 15], 9)
Solution().twoSum([2, 1, 1, 9], 2)

#---------------------------------------------------------------------

## 复制原数组信息后，排序双指针求出所需的数字，然后再从原数组获得index
## 时间复杂度O(nlogn)，空间复杂度O(n)

class Solution:
    def twoSum(self, nums, target):
        src_nums = nums.copy() #复制原数组，这里需要额外空间O(n)
        n = len(nums)
        nums.sort()
        
        # 通过双指针（O(n)）找到所需的两个数字
        i = 0
        while i < n:
            j = i + 1
            while nums[i] + nums[j] < target:
                j += 1
            if nums[i] + nums[j] == target:
                two_number = [nums[i], nums[j]]
                break
            i += 1

        # 从原数组中找到对应的index，注意这里会有两数相等的情况，所以取得第一个数后，将其置换为None
        idx1 = src_nums.index(two_number[0])
        src_nums[idx1] = None
        idx2 = src_nums.index(two_number[1]) 
        
        return [idx1, idx2] 
        

Solution().twoSum([2, 7, 11, 15], 9)
Solution().twoSum([2, 1, 1, 9], 2)


#---------------------------------------------------------------------

## 考虑一下开头所说的，如果没有两数相等的情况下，构建value: index的哈希表，然后对于每一个数字x，
## 如果target - x在哈希表中，输出对应的值即可，可以很快解决问题
## 那么有两数相等会产生什么情况呢，看以下的例子
# a = [2, 7, 11, 15]
# dict_a = {v: i for i, v in enumerate(a)}
# print(dict_a)  # {2: 0, 7: 1, 11: 2, 15: 3}，结果如预期所料

# b = [2, 1, 1, 9]
# dict_b = {v: i for i, v in enumerate(b)}
# print(dict_b)  # {2: 0, 1: 2, 9: 3}，可以看到第一个1原本对应的1:1被覆盖掉了

## 我们可以考虑下，如果x与y相等，x与y必定满足x + y = target，所以这两个数字就是我们要求的数字。
## 原因是，如果存在z满足 x + z = target的话，y + z = target也成立，这个和每种输入只会对应一个答案矛盾。
## 因此，我们可以构建一个异常处理，逐步构建哈希表，当发现有发生冲突时，此时即可return答案。
## 除此之外的情况，只需构建完哈希表后，遍历哈希表，对每一个k，找到target - k是否在哈希表中即可

## 时间复杂度 O(n),空间复杂度O(n)

class Solution:
    def twoSum(self, nums, target):
        value_idx = {} # 初始化哈希表
        for idx, i in enumerate(nums): # 逐一添加元素到哈希表
            if i in value_idx: # 如果发生冲突，return答案
                return [value_idx[i], idx]
            value_idx[i] = idx # 以value：index对形式添加
        
        for i in value_idx: # 遍历哈希表，return答案
            if target - i in value_idx:
                return [value_idx[i], value_idx[target - i]]


Solution().twoSum([2, 7, 11, 15], 9)
Solution().twoSum([2, 1, 1, 9], 2)


## 在此之上，我们再考虑第二个问题，上述对先构建完哈希表（同时注意异常处理），再遍历求解，有没有必要？
## 答案是，没有。事实上，我们可以在构建哈希表的同时，一边验证是否有异常，一边求解。
## 问题的关键点在于，下述异常发生时，
## 
## if i in value_idx: # 如果发生冲突，return答案
##     return [value_idx[i], idx]
## 意味着 target - i in value_idx也成立。而这个也是我们遍历哈希表时的判定条件。因此，两者可以同时进行。

## 时间复杂度 O(n),空间复杂度O(n)

class Solution:
    def twoSum(self, nums, target):
        value_idx = {}  # 初始化哈希表
        for idx, i in enumerate(nums): # 逐一添加元素到哈希表
            if target - i in value_idx: # 如果target - i存在哈希表中，return答案，此时考虑了冲突的情况
                return [value_idx[target - i], idx]
            value_idx[i] = idx  # 以value：index对形式添加
            

Solution().twoSum([2, 7, 11, 15], 9)
Solution().twoSum([2, 1, 1, 9], 2)
