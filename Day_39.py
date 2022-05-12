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

根據變數之間的除法關係 (紀錄於 pairs 及 quotients)，計算任意兩變數 (紀錄於 queries) 的商。

例如給定 x / y = 2.0 及 y / z = 5.0，並要求計算 x / z 及 z / x 的商，input 表示方法為:

pairs = [["x", "y"], ["y", "z"]]
quotients = [2.0, 5.0]
queries = [["x", "z"], ["z", "x"]]
Constraints:

可假設 input 都是合理的，不會出現除數為 0 或是矛盾的狀況
len(pairs) == len(quotients) 為 True
若 queries 中的變數不存在於 pairs 中，return -1.0
Example 1:

Input:
    - pairs = [["x", "y"], ["y", "z"]]
    - quotients = [2.0, 5.0]
    - queries = [["x", "z"], ["z", "x"], ["y", "x"], ["z", "w"]] 
Output: [10.0, 0.1, 0.5, -1.0]
Explanation:
題目給定 x / y = 2.0 及 y / z = 5.0, 並要求計算 x / z,  z / x, y / x, 和 z / w 的商,
前三個 queries 答案為 10.0, 0.1, 0.5，而最後一個 query 由於 "w" 並不存在 pairs 中，所以 return -1.0
Function Signature
class Solution:
    
    # @param pairs: List[List[str]]
    # @param quotients: List[float]
    # @param queries: List[List[str]]
    # @return List[float]
    def evaluateDivision(self, pairs, quotients, queries):
        # Implement me
'''