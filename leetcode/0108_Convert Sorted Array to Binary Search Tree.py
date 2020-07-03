"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


## 基本思想就是递归，选择数组中间的数字作为根节点，然后左右两侧的数组分别放到左右两边
# def 做一棵树（数组的哪个段落要做成树）：  
#     #some code 判断是否终止 
#     树的根部 = 这个段落A最中间的部分
#     树的左边 = 做一棵树（这个段落A的左边部分）
#     树的右边 = 做一棵树（这个段落A的右边部分）
#     return 这棵树


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:    
        def make_tree(left, right): # 制作树的递归函数
            if left > right: # left > right时停止
                return
            mid = (left + right) // 2 # 选择中间位置左边的数字作为根节点
            t = TreeNode(nums[mid]) # 将中间的数字作为根节点
            t.left = make_tree(left, mid - 1) # 制作左子树
            t.right = make_tree(mid + 1, right) # 制作右子树
            return t
        n = len(nums)
        return make_tree(0, n - 1)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def make_tree(left, right): # 制作树的递归函数
            if left > right: # left > right时停止
                return
            mid = (left + right + 1) // 2  # 选择中间位置右边的数字作为根节点
            t = TreeNode(nums[mid])  # 将中间的数字作为根节点
            t.left = make_tree(left, mid - 1)  # 制作左子树
            t.right = make_tree(mid + 1, right)  # 制作右子树
            return t
        n = len(nums)
        return make_tree(0, n - 1)


t = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
