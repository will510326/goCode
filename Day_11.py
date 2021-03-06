'''
這道題目曾出現在 DRW 的面試中。

一位藝術家在畫布上用素描勾勒出了城市的 skyline (天際線)，接著他想用最少 "水平筆畫" (horizontal stroke) 將此 skyline 上色，請問他最少需要畫幾筆？

skyline 是一個 positive integer array，其值代表城市的高度
畫筆的粗度相當於 1 單位的城市高度
一個筆畫的定義：下筆為筆畫的開始，起筆為筆畫的結束，中間不得中斷
水平筆畫的定義：從左往右或從右往左的筆畫
時間複雜度要求為 O(n)
Example 1:

Input: skyline = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]

  5                            +---+
                               |   |
  4                            |   |       +---+
                               |   |       |   |
  3        +---+               |   +-------+   |
           |   |               |               |
  2        |   +---+   +---+   |               +---+
           |       |   |   |   |                   |
  1    +---+       +---+   +---+                   |
       |                                           |
  0    +-------------------------------------------+
         0   1   2   3   4   5   6   7   8   9  10

Output: 9
Explanation: 我們可以由下往上開始畫，若遇到不連續的 skyline，則必須中斷筆畫，繪畫過程如下圖：

  5                            +---+
                               | 9 |
  4                            |---|       +---+
                               | 7 |       | 8 |
  3        +---+               |---+-------+---|
           | 5 |               |       6       |
  2        |---+---+   +---+   |---------------+---+
           |   2   |   | 3 |   |        4          |
  1    +---+-------+---+---+---+-------------------|
       |                     1                     |
  0    +-------------------------------------------+
         0   1   2   3   4   5   6   7   8   9  10

從圖中可看出我們需要 9 horizontal strokes 來完成上色。
Example 2:

Input: skyline = [1, 1, 2, 1, 1]

  2            +---+ 
               |   |
  1    +-------+   +-------+
       |                   |
  0    +-------------------+
         0   1   2   3   4  

Output: 2
Explanation: 由下往上開始畫，若遇到不連續的 skyline，則必須中斷筆畫，繪畫過程如下圖：

  2            +---+ 
               | 2 |
  1    +-------+---+-------+
       |         1         |
  0    +-------------------+
         0   1   2   3   4  

從圖中可看出我們需要 2 horizontal strokes 來完成上色。
Function Signature
class Solution:

    # @param skyline: List[int]
    # @return int
    def paintSkyline(self, skyline):
        # Implement me
'''