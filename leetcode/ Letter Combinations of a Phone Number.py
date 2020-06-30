"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

1        2: abc  3: def
4: ghi   5: jkl  6: mno
7: pqrs  8: tuv  9: wxyz

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

## 使用product当然可以解决问题，但这应该不是我们想要的
from itertools import product

class Solution:
    def letterCombinations(self, digits):
        digit_to_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        letters = [digit_to_letter[i] for i in digits]
        if letters:
            res = [''.join(i) for i in product(*letters)]
            return res
        else:
            return []
            
## 这道题考察的要点是回溯算法
## 回溯算法的框架如下，在解决排列组合问题时常用
# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return

#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择
# 当然写法很灵活，可参考Nqueen问题


Solution().letterCombinations('23')


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        digit_to_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []
        def backtrack(comb, nextdigit):
            if not nextdigit:
               res.append(''.join(comb))
            
            else:
                for letter in digit_to_letter[nextdigit[0]]:
                    comb.append(letter)
                    backtrack(comb, nextdigit[1:])
                    comb.pop()
        
        backtrack([], digits)
        return res
    

Solution().letterCombinations('23')

##  当然上面的backtrack是严格按照框架来的
## 所以用list来存储，用append，pop实现选择和撤销
## 其实考虑到本题的特征，我们不用选择撤销，因为要实现的是全排列
## 我们可以直接在不改变comb的情况下，直接对comb+letter进行回溯
## 这样的好处是，避免来选择和回撤的操作
## 然而本题可以这样做的原因，再强调一遍，因为是全排列，所有情况都满足要求

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_to_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(comb, nextdigit):
            if not nextdigit:
               res.append(comb)

            else:
                for letter in digit_to_letter[nextdigit[0]]:
                    backtrack(comb + letter, nextdigit[1:])
                    
        backtrack('', digits)
        return res


Solution().letterCombinations('23')

## 一般而言，我们是需要选择和回撤的，因为不是所有情况都满足要求的
## 举例来说，Nqueen问题和数组问题，也都可以通过回溯来解决