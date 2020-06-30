"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
    [-1, 0, 1],
    [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https: // leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


## 暴力穷举
## 三重循环
## 时间复杂度O (n^3)， 空间复杂度 O(1)
class Solution:
    def threeSum(self, nums):
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            for j in range(i + 1,  n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
        return res


Solution().threeSum([-1, 0, 1, 2, -1, -4])


# --------------------------------------------------------------------------------------
## 三指针问题（外部for循环，内部while双指针）
## 首先排序是O(nlogn)的，值得一做并且是双指针的必要条件
## 从nums的第i个元素起通过for遍历，先使得j, k = i + 1, len(nums) - 1
## while j < k，j和k分别向左和向右移动，如果满足nums[i] + nums[j] + nums[k] == 0则输出
## 当这个和比0大时，k向左，比0小时，j向右，直至j == k
## 这是一个基础的三指针问题，然而有很多可以优化的点
## 1.去重j, k，每次移动i，j，k，我们都应当考虑，nums[i], nums[j], nums[k]的值是否改变
## 2.剪枝i
##       2.1当nums[i] > 0时，nums[i]  + nums[j] + nums[k] > 0必然成立，因此可以break
##       2.2当i > 0且nums[i] == nums[i - 1]时，此时求得的关于i，j，k的值和i - 1的情况相同，因此可以continue
##       2.3当nums[i] + nums[k - 1] + nums[k] < 0，此时再怎么移动j也不会达到和为0，因此可以continue
##       2.4当nums[i] + num[j] + nums[j + 1] > 0，此时i右边任意3数的和必定大于0，因此可以break

## 时间复杂度 O(n^2)，空间复杂度O(1)
class Solution:
    def threeSum(self, nums):
        res = [] # 初始化res
        n = len(nums) # 获取数组长度
        nums.sort() # 排序
        
        for i in range(n - 2): # 第一重指针用for循环
            if i > 0 and nums[i] == nums[i - 1]: # 剪枝2.1
                continue

            if nums[i] > 0: # 剪枝2.2
                break

            k = n - 1
            if nums[i] + nums[k - 1] + nums[k] < 0: # 剪枝2.3
                continue
            
            j = i + 1 
            if nums[i] + nums[j] + nums[j + 1] > 0: # 剪枝2.4
                break


            while j < k: # 双指针用while循环
                sums = nums[i] + nums[j] + nums[k] # 求和
                if sums == 0: # 如果为0，则添加候选项进res
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1 # 向右移动j并且去重
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    k -= 1 # 向左移动k并且去重
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
                elif sums < 0: # sums < 0说明需要向右移动j
                    j += 1  # 向右移动j并且去重
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                else: # sums > 0 说明需要向左移动k
                    k -= 1  # 向左移动k并且去重
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
        return res # 返回res



Solution().threeSum([0, 0, 0,0])
Solution().threeSum([-1, 0, 1, 2, -1, -4])                 
Solution().threeSum([-1, 0, -1, 2, 1, 3, -3, 2, -1, -4])
Solution().threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0])



## 计数后排序优化
## 首先统计每个数字出现的次数（实践表明Counter太慢了，用defaultdict自己构建比较好）
## 为了保证res中没有重复要素，我们可以规定[i, j, k]满足i <= j <= k，所以需要对keys（即数字本身）做排序
## 接下来，对于每一个i，我们遍历j >= i的部分，如果 -(i - j)在keys中，且满足次数要求，则添加入res
## 这里比较绕的就是次数要求，首先遍历j之前，i的次数要减去1，这是为了防止j与i使用同一个原本只出现1次的数字
## 其次，如果 k > j，则k的次数也要1次以上，如果k == j，则此时j的次数要2次以上（这包含了i==j==k）的情况）
## 最后，作为优化，我们可以添加一些剪枝操作，如i > 0 或 k < j的话就直接break

## Counter版本花的时间比三指针还长

# from collections import Counter

# class Solution:
#     def threeSum(self, nums):
#         res = []
#         cnter = Counter(nums)
#         keys = sorted(cnter.keys())
        
#         for idx, i in enumerate(keys):
#             if i > 0:
#                 break

#             for j in keys[idx:]:
#                 cnter[i] -= 1
                
#                 if cnter[j] >= 1:
#                     k = - i - j
#                     if k < j:
#                         break
#                     if k > j and cnter[k] >= 1 or k == j and cnter[j] >= 2:
#                         res.append([i, j, k])
#         return res


from collections import defaultdict

class Solution:
    def threeSum(self, nums):
        res = [] # 初始化res
        cnter =defaultdict(int) # 设置计数器
        for i in nums:
            cnter[i] += 1  
        keys = sorted(cnter.keys()) # 排序keys

        for idx, i in enumerate(keys): # 遍历i
            if i > 0: # 剪枝
                break

            for j in keys[idx:]: # 遍历满足j >= i的j，因为i和j可能相等
                cnter[i] -= 1 # i的次数减去1，防止i和j使用单一的相同数字

                if cnter[j] >= 1: # 如果j == i的情况，由于上面减去1了，这里就会使得cnter[j] == 0
                    k = - i - j # 获取k
                    if k < j: # 剪枝
                        break
                    if k > j and cnter[k] >= 1 or k == j and cnter[j] >= 2: # 判断大小与次数
                        res.append([i, j, k])
        return res # 返回res


Solution().threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0])
Solution().threeSum([-1, 0, 1, 2, -1, -4])
Solution().threeSum([-1, 0, -1, 2, 1, 3, -3, 2, -1, -4])
