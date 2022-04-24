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

給定一個 "包含多個二維座標" 的 array，return k 個最靠近原點 (0, 0) 的座標點。

距離的定義為 Euclidean Distance
Ex: 座標 (x, y) 與原點 (0, 0) 的距離為 sqrt((x - 0)^2 + (y - 0)^2)
Return 的 k 個座標不需要考慮順序
Constraints:

座標值均為 integer
k >= 1
Example 1:

Input: points = [[1, 1], [-2, -2], [-3, 1], [4, 2]], k = 2
Output: [[1, 1], [-2, -2]]
Explanation: [1, 1] 與 [-2, -2] 是距離原點的最近的 2 個座標點
Example 2:

Input: points = [[0, 0], [-1, 1]], k = 3
Output: [[0, 0], [-1, 1]]
Explanation: k = 3，但只有兩個座標，所以 return 所有座標
Function Signature
class Solution:

    # @param points: List[List[int]]
    # @param k: int
    # @return List[List[int]]
    def findKClosest(self, points, k):
        # Implement me
'''