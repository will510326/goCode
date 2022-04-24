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

給定一個 sorted integer array nums，將 nums 中的連續數字以區間表示，最後 return 這些區間。

nums 中可能出現重複的數
Example 1:

Input: nums = [-5, -4, -1, 0, 1, 2, 3, 8, 10, 10, 11]
Output: ["-5->-4", "-1->3", "8", "10->11"]
Explanation: 一共有四個連續區間，區間可表示成 "該區間最小值->該區間最大值"。另外，由於 8 為該區間中唯一的數字，表示成 "8" 即可。
Example 2:

Input: nums = []
Output: []
Function Signature
class Solution:

    # @param nums: List[int]
    # @return List[str]
    def convertNumbersToRanges(self, nums):
        # Implement me
'''