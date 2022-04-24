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

這道題目曾出現在 Facebook 的面試中。

給定一個字母排序規則 order，驗證給定的 list of words 是否符合此排序規則 (由小至大排序)。

Constraints:

所有字母均為小寫字母，即 a 到 z
Example 1:

Input: words = ["go", "code"], order = "zyxwvutsrqponmlkjihgfedcba"
Output: True
Explanation: 根據 order，"g" 小於 "c"，所以此排序是正確的
Example 2:

Input: words = ["abc", "abz", "bcdefg", "bcde"], order = "abcdefghijklmnopqrstuvwxyz"
Output: False
Explanation:
    - "abc" < "abz"，因為 "c" 小於 "z"，符合排序規則
    - "anz" < "bcdefg"，因為 "a" 小於 "b"，符合排序規則
    - "bcdefg" > "bcde"，不符合排序規則，因為若前綴 (prefix) 相同，較長字串的 order 較大
由於有一項不符合排序規則，因此結果為 False
Function Signature
class Solution:

    # @param words: List[str]
    # @param order: str
    # @return bool
    def verifyWordOrdering(self, words, order):
        # Implement me
'''