"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

通过次数377,880提交次数647,577

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## 虽然不符合题目的进阶要求，转换为字符串是最简单的方法

class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

Solution().isPalindrome(121)
Solution().isPalindrome(-121)
Solution().isPalindrome(10)

## 反转数字，然后比较也可完成题目要求


class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        x_origin = x
        while x != 0: 
            x_last = x % 10
            reverse = reverse * 10 + x_last
            x = x // 10
        return reverse == x_origin
    

Solution().isPalindrome(121)
Solution().isPalindrome(-121)
Solution().isPalindrome(10)

Solution().isPalindrome(2e400) # 时间太长


## 但是当数字过大时，不仅计算时间长，且可能产生整数溢出(?)的问题
## 一个有效的解决方法是，反转一半数字的即可
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x!= 0):
            return False
        
        half_reverse = 0
        while half_reverse < x:
            x_last = x % 10
            half_reverse = half_reverse * 10 + x_last
            x = x // 10
        
        ## 反转完一半数字后，由于x的奇偶性，half_reverse >= x，分别对应处理即可
        if half_reverse > x:
            return (half_reverse // 10) == x
        else:
            return half_reverse == x


Solution().isPalindrome(121)
Solution().isPalindrome(-121)
Solution().isPalindrome(10)
Solution().isPalindrome(0)
Solution().isPalindrome(2e400)
