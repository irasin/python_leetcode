"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## 动态规划
## 用dp二维数组来记录，s的前i位和p的前j位能否匹配
## 目标就是从dp左上角计算到右下角
## 首先定义dp数组, dp.shape = (m + 1) * (n + 1)
## + 1的原因是为了记录空串
## 初始化都为False
## dp[0][0]为True，当p的前i为都为*时，dp[0][i]为True

## 状态转移方程
## p[j - 1]为字母时，当和s[i - 1]字母相同时，dp[i][j] = dp[i - 1][j - 1]
## p[j - 1]为?时，dp[i][j] = dp[i - 1][j - 1]，这个可以和第一种情况合并
## p[j - 1]为*时，
## 当*匹配空串时，dp[i][j] = dp[i][j - 1]，
## 当*匹配某字母时，dp[i][j] = dp[i - 1][j]，
## 这里[i - 1][j]的意思当前的*匹配了s的最后一个字符，
## 甚至来说，其实index >= i的dp[index][j]的值都变成了True，因为*可以匹配任意长字符串
## 所以从dp二维数组的角度来说就是这一列从index >= i的部分的值都变成了True

## 时间复杂度O(MN)，空间复杂度O(MN)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)] # 初始化dp，m行n列
        dp[0][0] = True # 空子串互相匹配，所以为真
        for i in range(1, n + 1): # p的前i个都为*，可匹配s为空串的情况，所以dp[0][i]为True
            if p[i - 1] == '*':  
                dp[0][i] = True 
            else:
                break
        for i in range(1, m + 1): # 计算状态转移
            for j in range(1, n + 1):  
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]: # 当p[j - 1]为？或者与s[i - 1]相同
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*': # 当p[j - 1]为*
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                # else: dp[i][j] = False  # 由于初始化dp为False，这个else可以不写
        return dp[m][n]
    


## 贪心算法
## 以*分割s

## 平均时间复杂度 O(MlogN), 空间复杂度 O(1)

