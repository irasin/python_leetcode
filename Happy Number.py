"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## 其实题目中写了解法了，重复计算，直到为1或者遇到曾经出现过的数进入无限循环

## 这种算法其实有风险，比如memory可能无法足够存储数
class Solution:
    def isHappy(self, n):
        memory = [] # 初始化记录表
        nums = str(n) # 转换为字符串方便取各个位的数字
        
        while True:
            res = sum([int(i) ** 2 for i in nums]) # 记录各个位平方和
            if res == 1: # 是快乐数
                return True
            elif res in memory: # 已出现过
                return False
            else: # 既不是1，也没有出现过
                memory.append(res) # 添加进记录表
                nums = str(res)  # 继续计算
                
                
Solution().isHappy(3)

## 快慢指针
## 用于链表找环的算法
## 快指针走两步，慢指针走一步，重复，如果快慢指针的值相等就停止循环
## 此时如果值都等于1，则为快乐数，如果不是1，则说明不是快乐数

## 这种算法的好处是，所需空间复杂度为O(1)

class Solution:
    def isHappy(self, n):
        slow, fast = n, n
        while True:
            slow = self.nextnumber(slow)
            fast = self.nextnumber(self.nextnumber(fast))
            if slow == fast:
                break
        if slow == 1:
            return True
        else:
            return False    
    
    def nextnumber(self, n):
        res = 0
        while n != 0:
            res += (n % 10) ** 2
            n //= 10
        return res
    

Solution().isHappy(19)

## 另外记录下求各个位上平方和的方法
## 事实上转换为str后计算太花时间了

# import time

# def timeit(fn):
#     def inner(n):
#         time1 = time.time()
#         fn(n)
#         time2 = time.time()
#         print(f'timeit = {time2 - time1}')
    
#     return inner

# @timeit
# def nextnumber1(n):
#     nums = str(n)
#     return sum([int(i) ** 2 for i in nums])

# @timeit
# def nextnumber(n):
#     res = 0
#     while n != 0:
#         res += (n % 10) ** 2
#         n //= 10
#     return res



# nextnumber1 (24124545245) # timeit = 5.1021575927734375e-05
# nextnumber(24124545245) # timeit = 1.4781951904296875e-05

