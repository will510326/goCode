'''
這道題目曾出現在 Facebook 的面試中。

給定 Binary Tree 的根節點 root, 找出包含所有 deepest nodes 的 subtree, 且此 subtree 必須是 minimum size subtree, 最後 return 此 subtree 的根節點.

Deepest nodes 是距離 root 最遠的節點
Subtree size 的定義為節點的總數量
有可能存在多個包含 deepest nodes 的 subtree, 我們的目標是要找到 minimum size subtree
Constraints:

保證 root 一定存在, 不會為空
Example 1:

Input: binary tree = 

    Level 0         9 (root)
                   / \
    Level 1       8   7
                 /   / \
    Level 2     6   5   4
                   / \   \
    Level 3       3   2   1

Output: 7
Explanation: Deepest nodes 為 node 3, 2, 及 1, 包含這三個 nodes 的最小 subtree 的 root 為 7
Note: Return type 為 TreeNode 而非 integer
Example 2:

Input: binary tree = 

    Level 0         9 (root)
                   / \
    Level 1       8   7
                 /
    Level 2     6

Output: 6
Explanation: Deepest node 為 node 6, 包含這個 node 的最小 subtree 的 root 為 6 本身, 所以 return 6
Note: Return type 為 TreeNode 而非 integer
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
    # @return TreeNode
    def findSmallestSubtreeWithAllDeepestNodes(self, root):
        # Implement me
'''