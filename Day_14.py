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

將給定的字串進行切割，目標是切出最多段 substring，切割的條件為 "每一種 character 僅能出現在一個 substring 內"，最後 return 切割後各 substring 的長度。

若 input 字串為空，則 return 一個空的 array
時間複雜度要求為 O(n)
Constraints:

所有 character 都是英文小寫字母，即 a 到 z
Example 1:

Input: "ababcbacadefegdehijhklij"
Output: [9, 7, 8]
Explanation:
此字串可以被切割成三段 substring，分別為 "ababcbaca" (長度 9)，"defegde" (長度 7)，及 "hijhklij" (長度 8)
    - "a", "b", "c" 僅存在於第 1 個 substring
    - "d", "e", "f", "g" 僅存在於第 2 個 substring
    - "h", "i", "j", "k", "l" 僅存在於第 3 個 substring
Note: 根據切割條件，也可以切成 "ababcbacadefegde" 及 "hijhklij"，但是這樣只有兩段，題目的要求是切成最多段
Function Signature
class Solution:

    # @param s: str
    # @return List[int]
    def partitionString(self, s):
        # Implement me
'''