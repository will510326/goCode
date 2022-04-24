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

這道題目曾出現在 Amazon 的面試中。

給定一個字串 array，將互相為 anagram 的字串分在同一組，最後 return 分組後的結果。

Anagram 的定義是兩個字串所包含的字母及各字母的數量都是一樣的，只是位置不同
例如 abc 及 cba 互相為 anagram，而 abc 及 cbc 互相不為 anagram
最終答案可以用任意順序排列
Example 1:

Input: ["dog", "ban", "banana", "nba", "ananab", "nnabaa", "god"]
Output: [["dog", "god"], ["banana", "ananab", "nnabaa"], ["ban", "nba"]]
Explanation:
["dog", "god"] 可分為一組，因為兩字串都各有 1 個 d, 1 個 o, 及 1 個 g
["banana", "ananab", "nnabaa"] 及 ["ban", "nba"] 也同理
Function Signature
class Solution:

    # @param strings: List[str]
    # @return List[List[str]]
    def groupAnagrams(self, strings):
        # Implement me
'''