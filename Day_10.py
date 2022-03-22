"""
這道題目曾出現在 DRW 的面試中。

將 input string 根據以下 transition rules 轉態，直到無法再轉態為止。此 string 只會存在 "A"，"B"，"C" 或 "D" 四種字元。

Rule 1：若 "A" 和 "B" 相鄰，轉態為 empty string
Rule 2：若 "C" 和 "D" 相鄰，轉態為 empty string
時間複雜度要求為 O(n)
Example 1:

Input: "CABADCBD"
Output: ""
Explanation: "CABADCBD" -> "CADCBD" -> "CABD" -> "CD" -> ""
Example 2:

Input: "ACBD"
Output: "ACBD"
Explanation: "A" 和 "B" 以及 "C" 和 "D" 均沒有相鄰，無法轉態
Function Signature
class Solution:

    # @param s: str
    # @return str
    def reduceString(self, s):
        # Implement me
"""

