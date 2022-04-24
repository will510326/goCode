'''
Hey Wayne，你今天刷題了嗎？

今天的題目如下

建議使用你熟悉的編輯器

根據定義好的 Function Signature 實現功能

練習效果會更好哦！

若有需要，我們也有提供付費詳解

請點下方連結查看詳細資訊！

50 題精選
祝刷題愉快：）

​

- goCode 趣刷題

這道題目曾出現在 Bloomberg 的面試中。

將給定的 encoded string 進行解碼 (decode)，return 解碼後的 string。

Encoded string 可表示為 k[encodedString]，解碼後所得到的 string 為括號內的 string 重複 k 次
Constraints:

k 為用字串表示的正整數
encodedString 中，可能存在的字母範圍為 a-z 及 A-Z
Example 1:

Input: "a2[B2[c]]"
Output: "aBccBcc"
Explanation: "a2[B2[c]]" -> "a2[Bcc]" -> "aBccBcc"
Example 2:

Input: "a2[bc]12[d]"
Output: "abcbcdddddddddddd"
Explanation: "a2[bc]12[d]" -> "abcbc12[d]" -> "abcbcdddddddddddd"
Function Signature
class Solution:

    # @param s: str
    # @return str
    def decodeString(self, s):
        # Implement me
'''