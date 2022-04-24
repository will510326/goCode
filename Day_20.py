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

類似題目曾出現在 Google 的面試中。

給定一個迷宮 maze、起點 A、及終點 B，尋找從 A 到 B 的最短路徑。maze 中的 0 代表可通行的路徑，1 代表不可通行的牆壁。

可能存在多個最短路徑，return 其中一個即可
可能不存在由 A 通往 B 的路徑，此時 return 空字串 "" 即可
完整的 input/output format 請參考 example 及 function signature
Constraints:

A 及 B 座標在 maze 上的值必定為 0
保證 maze 不為空
Example 1:

Input: 
    maze = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 0, 0, 1]],
    A = [0, 2],
    B = [1, 1]
Output: "(0,2)->(0,3)->(1,3)->(2,3)->(2,2)->(2,1)->(1,1)"
Example 2:

Input: 
    maze = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 0, 0, 1]],
    A = [0, 0],
    B = [0, 2]
Output: ""
Explanation: (0, 0) 沒有任何路徑可以抵達 (0, 2)，所以 return ""
Function Signature
class Solution:
    
    # @param maze: List[List[int]]
    # @param A: List[int]
    # @param B: List[int]
    # @return str
    def findShortestPath(self, maze, A, B):
        # Implement me
'''