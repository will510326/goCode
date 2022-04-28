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

這道題目曾出現在 Microsoft 的面試中。

給定一個大小為 m x n 的 sorted matrix 及一個 target，檢查 target 是否存在於 matrix 中，若存在則 return True；否則 retrun False。

Time complexity 要求:
Basic: O(mlogn) 或 O(nlogm)
Optimal: O(m + n)
Sorted matrix 的特性為:
每個 row 由左至右遞增
每個 column 由上至下遞增
Constraints:

matrix 中的值以及 target 均為 int
Example 1:

Input: target = -2, matrix = [
  [-10, -9,  0,  2,  8],
  [ -7, -2,  1,  4,  9],
  [ -2,  1,  2,  5, 11],
  [  2,  8, 10, 13, 15],
  [ 10, 20, 30, 31, 32]]
Output: True
Explanation: -2 存在於 matrix 中，所以 return True
Example 2:

Input: target = -3, matrix = [
  [-10, -9,  0,  2,  8],
  [ -7, -2,  1,  4,  9],
  [ -2,  1,  2,  5, 11],
  [  2,  8, 10, 13, 15],
  [ 10, 20, 30, 31, 32]]
Output: False
Explanation: -3 不存在於 matrix 中，所以 return False
Function Signature
class Solution:
    
    # @param matrix: List[List[int]]
    # @param target: int
    # @return bool
    def searchInASorted2DMatrix(self, matrix, target):
        # Implement me
'''