"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
 

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n ** 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## matrix直接flatten成vector然后排序即可
## 时间复杂度 O(n**2logn) 空间复杂度 O(n**2)

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        matrix = [i for j in matrix for i in j]
        matrix.sort()
        return matrix[k - 1]
        
 
matrix = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8

Solution().kthSmallest(matrix, k)

## 堆排序优化的分治
## matrix中的每个子数组都是排好序的，所以可以利用merge sort的思想来归并，减少排序时间
## 但是两两归并的话，时间会很慢
## 这里是n个数组归并，所以可以用n个最小根堆来维护
## 还是不太熟悉heap的原理，所以这里未实现


class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        merged = []
        for i in range(n):
            merged = self.merge(matrix[i], merged)
            
        return merged[k - 1]
    
    def merge(self, m, n):
        merged = []
        size_m = len(m)
        size_n = len(n)
        i, j = 0, 0
        while i < size_m and j < size_n:
            if m[i] <= n[j]:
                merged.append(m[i])
                i += 1
            else:
                merged.append(n[j])
                j += 1
        if i < size_m:
            merged.extend(m[i:])
        if j < size_n:
            merged.extend(n[j:])
        return merged


## 二分法
## 注意到这个matrix的特性是
## matrix[0][0]最小，matrix[n - 1][n - 1]最大
## 而当matrix[i][j]的要素为x时， 不超过x的要素都在matrix的左上三角的部分
## 这就意味着，x往上的这一列的元素，都会不超过x，且其个数为i + 1
## 虽然左上三角的部分不是标准三角，会被分割成不规则的形状
## 但是我们可以从左下到右上，输出不超过x的要素的个数
## 如果这个个数小于k，则要找的元素在x的右下部分
## 如过这个个数大于k，则要找的元素在x的左上部分
## 举例来说
## 1 2 3 4
## 3 4 5 6
## 7 7 8 9
## 如果要找 是第9大的元素，
## 最小的元素为low = 1, 最大的元素为high = 9,mid = (1 + 9) // 2 = 5
## 这个时候，从坐下往右上查找不超过5的元素个数

# n = len(matrix)
# i, j = n - 1, 0
# cnt = 0
# while i >= 0 and j < n: # 从坐下到右上遍历
#   if matrix[i][j] <= mid:
#       cnt += i + 1  # 加上当前列的小于等于mid的元素个数
#       j += 1        # 移动到下一列
#   else:
#       i -=1         # 移动到上一行

# 顺带一提，还有逐行检查的方法，但效率比较低
# n = len(matrix)
# i, j = n - 1, 0
# cnt = 0
# while i >= 0
#     while j < n and matrix[i][j] <= mid:
#         cnt += 1
#         j += 1
#     i -= 1
#     j = 0

## 或者是用for
# cnt = 0
# for i in range(n - 1):
#     for j in range(n - 1):
#         if matrix[i][j] <= mid:
#             cnt += 1
#         else:
#             break
        


## 如果cnt < k，则要找的元素 > mid，即在右下部分，令low = mid + 1
## 如果cnt >= k，则要找的元素<= mid，即在左上部分，令high = mid
## 重复上述的结果直至low == high

## 可以得到，不超过5的元素个数为7，7 < 9，所以令low = 5 + 1 = 6
## mid = (6 + 9) // 2 = 7 
## 继续，不超过7的元素个数为10，10 > 9，所以令high = 7
## mid = (6 + 7) // 2 = 6
##  继续，不超过6的元素个数为8，8 < 9，所以令low = 7
## low == high，所以输出7

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        def count(mid):
            i, j = n - 1, 0
            cnt = 0
            while i >= 0 and j < n:  # 从坐下到右上遍历
                if matrix[i][j] <= mid:
                    cnt += i + 1  # 加上当前列的小于等于mid的元素个数
                    j += 1        # 移动到下一列
                else:
                    i -= 1  # 移动到上一行
            return cnt
        
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            
            cnt = count(mid)
            if cnt >= k: # 如果cnt >= k，说明所求元素在左上区域
                high = mid
            else:        # 如果cnt < k，说明所求元素在右下区域
                low = mid + 1
        return low  
    

matrix = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
Solution().kthSmallest(matrix, k)
