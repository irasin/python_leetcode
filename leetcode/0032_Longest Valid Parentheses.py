"""

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


## 暴力穷举
## 从长到短，从左往右，检查子串是否是有效子串
## 检查的方法通过栈来实现

## 时间复杂度 O(N^3), 空间复杂度 O(N)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        
        def isValid(start, end): # 判断s[start: end]是不是有效的
            stack = [] # 使用stack来处理
            for i in range(start, end):
                if s[i] == '(': # 遇到左括号append
                    stack.append('(')
                elif stack != []: # 遇到右括号且stack不为空，pop最后一个左括号，即消除一对有效括号
                    stack.pop()
                else: # 遇到有括号，但stack为空了，说明无法匹配，s[start: end]在此处必定被分割，所以不是有效的
                    return False
            return stack == [] # 如果最后stack里还有左括号，则说明不是有效但

        for i in range(n if n % 2 == 0 else n - 1, 0, -2): # 倒序决定想建议的有效括号子串的长度，注意i必定为偶数
            for j in range(n - i + 1): # 从头开始，检查长度为i的子串是否有效，注意边界为 n - i + 1
                if isValid(j, j + i): # 若有效，则直接return子串长度，即为i
                    return i
        return 0 # 若无有效子串，return 0
                
        
        
## 动态规划
## 用dp数组，记录到每一位位置的最长有效子串的长度
## 首先初始化都为0
## 其次找到状态转移方程
## 如果遇到(，不会产生配对，不用更新
## 如果遇到)，要看是否与i - dp[i - 1] - 1产生配对，且i - dp[i - 1] - 1必须是有效的index，即不小于0
## 这里的 i - dp[i - 1] - 1中，dp[i - 1]代表前一位产生的有效匹配长度
## 举例来说， ...(())
## 最后一个)的index为i的话，与它配对的是i - 2 - 1 = i - 3，即倒数第四个字符，
## 如果满足上述条件，则更新式如下
## dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
## 这里第一项代表产生配对的()，长度为2，第二项代表被产生配对的()所包住的有效子串的长度，
## 第三项代表，产生配对的()前方相邻的有效子串的长度，这一项该怎么理解呢
## 其实意思就是，我们当前求得的配对的()可能也只是一个部分有效子串而已，和前面连在一起
## 依然拿上面的例子来说的话，就是...()(())，
## 求得了最后的)和倒数第四个字符(配对，但是前方还有一组()
## 所以dp[i] = 6才对
## 问题是，我们虽然保证了i - dp[i - 1] - 1 >= 0，
## 但是i - dp[i - 1] - 2可能等于-1，然而初始化的时候，正好初始化为0了，所以不会有bug

## 时间复杂度 O(N)，空间复杂度 O(N)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        dp = [0] * n # 初始化dp数组
        for i in range(n):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
        return max(dp)
        
## 栈
## 暴力穷举里的栈被用来检验子串是否有效
## 然而暴力穷举慢的原因是，没有利用子串不合格的这些信息
## 举例来说
## ())(()
## 这个情况下，暴力穷举从大到小，从左往右计算时，每次都会因为第二个)
## 导致i=6，4时判断是无效的
## 事实上，这些都是重复计算，完全可以保留这个无效信息，
## 从这个无效点开始，把s分割开来
## s之前的最长有效子串的长度，保存为res
## 然后找s之后的有效子串，并判断是不是最长就行了
## 如此一来，只需遍历一次s即可

## 时间复杂度 O(N)，空间复杂度 O(N)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        res = 0 # 最长子串的长度
        tmp_length = 0 # 记录找到的子串的长度
        stack = [-1] # stack初始化为只含有-1
        for i in range(n):
            if s[i] == '(': # 如果是(，记录当前index
                stack.append(i)
            else:  # 如果是)
                stack.pop() # pop掉stack最后的元素（-1或(的index）
                # 判断当前的)是否是合法的，
                if stack == []:  # 如果pop的是-1，stack变成[]，则说明没有配对，在此处分割
                    stack.append(i) # 如果分割的话，记录当前)的index，以此为开始重新计算之后的有效子串
                else:  # 如果pop的是(的index，说明完成配对，stack不为空，即有效。
                    tmp_length = i - stack[-1]  # 当前的)是合法的，则计算配对后的子串长度，
                    res = max(res, tmp_length) # 比较是否是最大子串长度
        return res
        

Solution().longestValidParentheses('((()))')
