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

在某些 Compiler Design 中, 我們會用 Binary Tree 來表示算式, 其中 Leaf Node 為數字, Internal Node 為 Operator, 這樣的 Binary Tree 稱為 Expression Tree. 給定 Expression Tree 的根節點 root, 請實現一個能計算此算式的 function.

Tree node 的 value 是 string type
Internal node 包含 "+", "-", "*", "/" 四種可能的 operators
Example 1:

Input: binary tree = 

    Level 0          "*" (root)
                   /     \
    Level 1      "-"     "/"
                 / \     / \
    Level 2    "5" "6" "3" "2"

Output: -1.5
Explanation: 此 binary tree 表達的是 (5 - 6) * (3 / 2) = (-1) * (1.5) = -1.5
Example 2:

Input: binary tree = 

    Level 0          "*" (root)
                   /     \
    Level 1      "-"     "/"
                 / \     / \
    Level 2    "5" "+" "3" "2"
                   / \
    Level 2     "10" "20"

Output: -37.5
Explanation: 此 binary tree 表達的是 (5 - (10 + 20)) * (3 / 2) = (-25) * (1.5) = -37.5
Function Signature
# Definition of a binary tree node
class TreeNode:

    # @param val: str
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    # @param root: TreeNode
    # @return float
    def evaluate(self, root):
        # Implement me
'''