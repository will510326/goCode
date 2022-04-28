'''
- goCode 趣刷題

這道題目曾出現在 Google 的面試中。

從給定的 words (list of strings) 中，找出 longest word chain 的長度。

字串串接 (chain) 的條件為:
若能藉由 "在 word1 任意位置中插入一個字母"，使得 word1 等於 word2，則 word2 可串接在 word1 後面
word1 稱為 word2 的 predecessor
word2 稱為 word1 的 succesor
Ex: fboo 可串接在 foo 後方
Word chain 是由許多字串組成的序列 (sequence)，這個序列由頭至尾的字串符合上述的字串串接條件
Ex: "foo" -> "fboo" -> "fboao" -> "fboaor" 是長度為 4 的 word chain
Constraints:

len(words) > 0
所有字串均由小寫英文字母所組成
定義單一字串為 "長度為 1 的 word chain"
Example 1:

Input: words = ["a", "b", "ca", "db", "eca", "fdb", "ecga"]
Output: 4
Explanation: Longest word chain 為 "a" -> "ca" -> "eca" -> "ecga"
Example 2:

Input: words = ["a", "b", "ca", "cb", "cab", "dcab"]
Output: 4
Explanation:
共有兩個 Longest word chain:
    1. "a" -> "ca" -> "cab" -> "dcab"
    2. "b" -> "cb" -> "cab" -> "dcab"
Function Signature
class Solution:
    
    # @param words: List[str]
    # @return int
    def findLongestWordChain(self, words):
        # Implement me
'''