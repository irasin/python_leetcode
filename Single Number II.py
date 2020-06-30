"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

##


##  和136题一样，使用set是一个很有趣的方法，但不符合要求
# class Solution:
#     def singleNumber(self, nums):
#         num_set = set(nums)
#         res = (sum(num_set) * 3 - sum(nums)) // 2
#         return res


## 可以通过一个通法解决某元素出现一次，其余元素出现k次
## 转换为二进制后，每一位上对k取模的结果就是所需求的数
## 但是，这个位运算不是很懂

# 时间复杂度O(N)，空间复杂度O(1)
class Solution:
    def singleNumber(self, nums):
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1 # 看最后一个bit为0或1
                num >>= 1 # 向右移位1个bit
        res, m = 0, 3
        print(counts)
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
            print(res)
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)



# 逻辑电路
"""
需要定义一种逻辑运算满足 1 * 1 * 1 = 0， 0 * 1 = 1

以00, 01, 10来表示出现0/3，1，2次，即XY表示状态时
X为1表示第二次出现，X为0且Y为1表示第一次出现

对于原本的每一个bit，我们用XY表示它的状态
由于一个数字最多出现三次，则只需考虑新状态为0（00）或 1（01）
则遇到新的状态转移如下

XY  Z  X' Y'
00  0  0  0
01  0  0  1
10  0  1  0
00  1  0  1
01  1  1  0
10  1  0  0


这个时候，考虑X'，Y'什么情况为真呢？根据真伪表的计算方式
比如，看Y'和（X, Y, Z)的关系
Y' = ~X & Y & ~Z  |  ~X & ~Y & Z = ~X &(Y & ~Z | ~Y & Z) = ~X & (Y^Z)
X' = X & ~Y & ~Z  |  ~X & Y & Z 

也就是说
每输入一个Z，可以做如下的迁移，计算方式如上
X，Y = X，Y‘
注意这里X，Y要同时更新

因为这样的话就是用更新过的Y来更新X，这样的话X的更新式需要变化
至于怎么变呢，其实只要看上述状态转移表中X'和（X Y' Z')的关系即可
可以发现
X = X & X |




最后，输出Y即可


"""

# 时间复杂度O(N)，空间复杂度O(1)

class Solution:
    def singleNumber(self, nums):
        X, Y = 0, 0
        for Z in nums:
            X, Y = (X & ~Y & ~Z) | (~X & Y & Z), ~X & (Y ^ Z)
        return Y


Solution().singleNumber([2, 2, -3, 2])

"""
注意这里X，Y要同时更新

因为这样的话就是用更新过的Y来更新X，这样的话X的更新式需要变化
至于怎么变呢，其实只要看上述状态转移表中X'和（X Y' Z')的关系即可

X  Z  X' Y'
0  0  0  0
0  0  0  1
1  0  1  0
0  1  0  1
0  1  1  0
1  1  0  0

X = X & ~Y' & ~Z | ~X & ~Y' & Z = ~Y' & (X & ~Z | ~X & Z) = ~Y' & (X ^ Z)

代码如下
"""
class Solution:
    def singleNumber(self, nums):
        X, Y = 0, 0
        for Z in nums:
            Y = ~X & (Y ^ Z)
            X = ~Y & (X ^ Z)
        return Y
    
Solution().singleNumber([2, 2, -3, 2])
