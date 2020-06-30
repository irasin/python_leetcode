"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
示例2:

 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
提示：

链表长度在[0, 20000]范围内。
链表元素在[0, 20000]范围内。
进阶：

如果不得使用临时缓冲区，该怎么解决？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## 只需记录每一个节点的值是否出现，然后剪枝即可
## 问题的关键是，不要检查当前节点的值，而是下一个节点的值
## 因此检查当前节点的值不满足条件是，需要将当前节点和上一节点断开，再把下一节点拼接上
## 即使得parent.next = current.next
## 这个操作涉及到上一节点，然而我们无法访问上一节点，所以我们无法实现
## 所以我们应该检查下一个节点的值
## 这样下一个节点不满足要求时，我们可以轻易地更新
## 即current.next = current.next.next

## 时间复杂度O(n)，空间复杂度O(n)

class Solution:
    def removeDuplicateNodes(self, head: ListNode):
        if not head: # 如果head为空，直接return
            return
        current = head # 初始化current
        visited = [current.val] # 初始化visited
        while current.next: # 当current下一个节点不为空
            if current.next.val in visited: # 判断下一个节点的val是否在visited中
                current.next = current.next.next # 如果在，则移除下一个节点，
            else:
                visited.append(current.next.val) # 如果不在，记录下一个节点的val
                current = current.next # 移动current到下一个节点
        return head
        


## 考虑一种不使用额外空间，即使得空间复杂度为O(1)的方法
## 那就必须牺牲时间了
## 可以双重遍历，对每一个节点，遍历这之后的节点，并且删除相同节点

## 时间复杂度 O(N^2)，然而不幸的是，python会超时

# class Solution:
#     def removeDuplicateNodes(self, head: ListNode):
#         if not head:
#             return
#         current = head # 初始化current
#         while current: # 遍历current，直至到末尾为None
#             rest = current # 初始化res，和第一个方法一样，要对rest.next进行判断，不然无法移除节点
#             while rest.next: # 当下一节点不为None
#                 if rest.next.val == current.val: 
#                     rest.next = rest.next.next
#                 else:
#                     rest = rest.next
#             current = current.next
#         return head
