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

從一個 integer array nums 中，找出最長的連續數列，並 return 其長度。

連續數列 (Consecutive Sequence) 定義: 數列由左至右遞增，且遞增值為 1
Ex: [-2, -1, 0, 1] 是 consecutive sequence
Ex: [1, 2, 3, 5] 不是 consecutive sequence
若 nums 為空，return 0
Time complexity 的要求為 O(n)
Example 1:

Input: nums = [11, -1, 12, 0, -2, 1, 13]
Output: 4
Explanation: 
nums 存在兩個連續數列: [-2, -1, 0, 1] 及 [11, 12, 13]
由於 [-2, -1, 0, 1] 長度較長，所以 return 其長度 4
Example 2:

Input: nums = [1, 3, 5, 7, 9]
Output: 1
Explanation: 
nums 存在五個連續數列: [1], [3], [5], [7], [9]
長度均為 1，所以 return 1
Function Signature
class Solution:

    # @param nums: List[int]
    # @return int
    def longestConsecutive(self, nums):
        # Implement me
'''