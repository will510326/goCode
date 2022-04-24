'''
這道題目曾出現在 Uber 的面試中。

給定一個括號字串，請移除最少數量的括號，使得整個括號字串是合理的 (valid)，最後 return 移除的數量。

合理 (valid) 的定義為每個左括號都有一個匹配的右括號
Constraints:

括號字串僅包含 "(" 或 ")" 兩種字元
Example 1:

Input: s = "())((()))"
Output: 1
Explanation: s[3] 沒有對應的左括號，其餘字串都有匹配的括號，所以 return 1
Example 2:

Input: s = "()((()))"
Output: 0
Explanation: s 是一個 valid 括號字串，不需要移除
Example 3:

Input: s = ")("
Output: 2
Explanation: s[0] 沒有對應的左括號，s[1] 沒有對應的右括號，所以 return 2
Function Signature
class Solution:

    # @param s: str
    # @return int
    def countMinimumRemovals(self, s):
        # Implement me

'''