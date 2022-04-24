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

給定一個 list of intervals，合併所有重疊的 intervals，最後 return 合併後結果。

Interval 表示方式：[x, y]
x < y
x 和 y 分別為 lower bound 和 upper bound
重疊的例子：
a = [1, 2], b = [2, 3]: a 和 b 有重疊，可合併為 [1, 3]
a = [1, 2], b = [3, 4]: a 和 b 沒有重疊，不可合併
時間複雜度要求為小於 O(n^2)，其中 n 為 interval 的個數
Example 1:

Input: [[1, 2], [2, 3], [3, 4], [5, 6]]
Output: [[1, 4], [5, 6]]
Explanation:
[1, 2], [2, 3], [3, 4] 可合併為 [1, 4]
[5, 6] 沒有跟別人重疊
Example 2:

Input: [[15, 18], [-5, 3], [0, 5], [7, 10], [6, 8]]
Output: [[-5, 5], [6, 10], [15, 18]]
Explanation:
[-5, 3] 和 [0, 5] 可以合併為 [-5, 5]
[6, 8] 和 [7, 10] 可以合併為 [6, 10]
[15, 18] 沒有跟別人重疊
Function Signature
class Solution:

    # @param intervals: List[List[int]]
    # @return List[List[int]]
    def mergeIntervals(self, intervals):
        # Implement me


'''