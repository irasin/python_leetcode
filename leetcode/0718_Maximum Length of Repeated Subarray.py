"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释: 
长度最长的公共子数组是 [3, 2, 1]。
说明:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


## 暴力穷举
## 同时注意，由于穷举的是index，要考虑边界条件为size+1，不然最后一个数取不到
## 但是会超时

## 时间复杂度 O(N^3)，空间复杂度O(1)

class Solution:
    def findLength(self, A, B):
        n_A = len(A)
        n_B = len(B)
        if not n_A or not n_B:
            return 0
        res = 0
        for i in range(n_A):
            for j in range(i + 1, n_A + 1):
                if j - i <= n_B:
                     for k in range(n_B):
                         if A[i: j] == B[k: k+ j - i]:
                             res = max(res, len(A[i: j]))
        return res
                            
          
                

Solution().findLength([1,2,3,4,2,1], [3, 2, 1,2, 3, 4])

Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])

## 动态规划
## dp也是要注意边界问题，一般是size + 1
## 同时本题的dp是一个二维矩阵
## 但这个题目既可以考虑从前往后dp，也可以从后往前dp
## 原因是因为，看两个数组是否相等，从前往后和从后往前是没有区别的

## 时间复杂度O(N*M),空间复杂度 O(N*M)

## 从前往后dp
## dp[i][j]代表A[:i]B[:j]的最长公共前缀
## 更新式如下
# if A[i] == B[j]:
#     dp[i + 1][j + 1] = dp[i][j] + 1
class Solution:
    def findLength(self, A, B):
        n_A = len(A)
        n_B = len(B)
        if not n_A or not n_B:
            return 0
        res = 0
        dp = [[0] * (n_B + 1) for _ in range(n_A + 1)]
        for i in range(n_A):
            for j in range(n_B):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    res = max(dp[i + 1][j + 1], res)
        return res

## 从后往前dp
## dp[i][j]代表A[i:]和B[j:]的最长公共前缀
## 更新式如下
# if A[i] == B[j]:
#     dp[i][j] = dp[i + 1][j + 1] + 1

class Solution:
    def findLength(self, A, B):
        n_A = len(A)
        n_B = len(B)
        if not n_A or not n_B:
            return 0
        res = 0
        dp = [[0] * (n_B + 1) for _ in range(n_A + 1)]
        for i in reversed(range(n_A)): # 注意是倒序的dp
            for j in reversed(range(n_B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    res = max(dp[i][j], res)
        return res
                

Solution().findLength([1, 2, 3, 4, 2, 1], [3, 2, 1, 2, 3, 4])

Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])


## 滑动窗口法
## 可以考虑一个问题，为什么暴力穷举需要那么多循环
## 是因为我们需要找到两个数列中最先相等的数,即对齐开头 ->O(N^2)，
## 然后看之后相等的数有多少 -> O(N)
## 这个时候我们可以选择，滑动窗口法
## 具体而言，某个数组的第i位对齐另一个数组B的第0位 -> O(N)
## 然后判断是否需要更新最长重复子数组 -> O(min(N, M))

## 这样时间复杂度就是两者相乘 O(N * min(N, M))，空间复杂度为O(1)
## 然后总的时间复杂度为O((N+M) * min(N, N))

class Solution:
    def findLength(self, A, B):
        n_A = len(A)
        n_B = len(B)
        if not n_A or not n_B:
            return 0
        else:
            return max(self.calc(A, B), self.calc(B, A))
    
    def calc(self, A, B):
        res = 0
        n_A = len(A)
        n_B = len(B)
        for i in range(n_A): # 较长数组的第i位对齐较短数组的第0位
            tmp = 0
            for m, n in zip(range(i, n_A), range(n_B)):
                # 判断是否需要更新最长子数组
                # 这里有个小技巧，使用tmp记录重复子数组的长度
                # 如果遇见不同元素，则将tmp重置为0，因为后面可能还会有重复子数组
                if A[m] == B[n]: 
                    tmp += 1
                    res = max(res, tmp)
                else:
                    tmp = 0
        return res
        
        
Solution().findLength([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
