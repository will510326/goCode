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

假設我們有一堆石頭，其重量可用 stones array 表示，有位小朋友每次都從這堆石頭中，挑選兩個最重的石頭互相碰撞，碰撞的規則如下:

若兩石頭的重量相同，碰撞後兩顆石頭都會完全粉碎
若兩石頭的重量不同，碰撞後只會剩下較重的那顆石頭，且該石頭重量會變成 "原本重量 - 較輕那顆石頭的重量"
這位小朋友不斷拿兩個最重的石頭互砸，直到僅剩一顆石頭或是所有石頭都粉碎為止，請計算最後那顆石頭的重量。

若最後沒有剩下的石頭，則 return 0
stones 中的元素代表石頭的重量
Time Complexity 的要求為 O(nlogn)
Constraints:

stones is a positive integer array
Example 1:

Input: stones = [2, 10, 4, 2, 20, 3]
Output: 1
Explanation: 
    Round 1: 挑選 10 及 20，互撞後的石頭重量為 10，stones 變成 [2, 4, 2, 10, 3]
    Round 2: 挑選 4 及 10，互撞後的石頭重量為 6，stones 變成 [2, 2, 6, 3]
    Round 3: 挑選 6 及 3，互撞後的石頭重量為 3，stones 變成 [2, 2, 3]
    Round 4: 挑選 2 及 3，互撞後的石頭重量為 1，stones 變成 [2, 1]
    Round 5: 挑選 2 及 1，互撞後的石頭重量為 5，stones 變成 [1]
    僅剩一個重量為 1 的石頭，所以 return 1
Example 2:

Input: stones = [100, 1, 2]
Output: 97
Explanation: 
    Round 1: 挑選 100 及 2，互撞後的石頭重量為 98，stones 變成 [98, 1]
    Round 2: 挑選 98 及 1，互撞後的石頭重量為 6，stones 變成 [97]
    僅剩一個重量為 97 的石頭，所以 return 97
Function Signature
class Solution:

    # @param stones: List[int]
    # @return int
    def smashStones(self, stones):
        # Implement me
'''