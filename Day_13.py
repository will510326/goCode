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

給定一個三角形 triangle，找出一條擁有最小 path sum 路徑，並 return 其值。

Path 的定義為從 triangle 頂點至底部所形成的路徑
triangle 為 2D array
Example 1:

Input: triangle = [
      [2],
     [3,4],
    [6,5,7],
   [4,1,8,3]]
Output: 11
Explanation: 最小的路徑由上至下為 2 -> 3 -> 5 -> 1，總和為 11
Note:
    - 2 的下一步可以選擇 3 或 4
    - 3 的下一步可以選擇 6 或 5 (不能選 7)
    - 5 的下一步可以選擇 1 或 8 (不能選 4 和 3)
    - 以此類推
Function Signature
class Solution:

    # @param triangle: List[List[int]]
    # @return int
    def findMinPathSumOfTriangle(self, triangle):
        # Implement me
'''