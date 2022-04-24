'''
這道題目曾出現在 Amazon 的面試中。

給定 Binary Tree 的根節點 root, 判斷此 Binary Tree 是否左右對稱 (以 root 為中心), 若對稱 return True, 否則 return False.

對稱包含 1) 結構對稱, 以及 2) 數值對稱
Empty tree 及 single node binary tree 皆屬於 symmetric binary tree
Time Complexity 的要求為 O(n)
Follow up:

使用 Recursion 及 Iteration 兩種方法解決這個問題
Example 1:

Input: binary tree = 

    Level 0         9 (root)
                   / \
    Level 1       8   8
                 /     \
    Level 2     6       6

Output: True
Explanation: 此 binary tree 在結構上與數值上都以 root 為中心對稱
Example 2:

Input: binary tree = 

    Level 0         9 (root)
                   / \
    Level 1       8   8
                 /
    Level 2     6

Output: False
Explanation: 此 binary tree 在結構上不對稱
Example 2:

Input: binary tree = 

    Level 0         9 (root)
                   / \
    Level 1       8   7
    
Output: False
Explanation: 此 binary tree 結構上是對稱的, 可是數值上不對稱
Function Signature
# Definition of a binary tree node
class TreeNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    # @param root: TreeNode
    # @return bool
    def isSymmetric(self, root):
        # Implement me

'''