'''
這道題目曾出現在 Facebook 的面試中。

給定一個字串 s，其中 s 只包含英文字母，左括號 "("，及右括號 ")"。

我們的任務是移除最少數量的 "(" 或 ")"，使得 s 中所有括號都匹配，最後 return 移除括號後的字串。

括號匹配的定義：所有的左(右)括號都存在一個與之對應的右(左)括號
Example 1:

Input: s = "(go(code))is(fantastic))"
Output: "(go(code))is(fantastic)"
Explanation: 最少需移除最後一個 ")"，才可使所有括號匹配
Example 2:

Input: s = "))go((code)"
Output: "go(code)"
Explanation: 最少需移除前兩個 ")" 及第一個 "("，才可使所有括號匹配
Example 3:

Input: s = ")))))g)(((((o("
Output: "go"
Explanation: 所有括號都不匹配，需全部刪除，最後只剩 "go"
Function Signature
class Solution:

    # @param s: str
    # @return str
    def removeMinParentheses(self, s):
        # Implement me
    
'''