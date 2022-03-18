"""
這道題目曾出現在 Amazon 的面試中。

給定 Binary Search Tree (BST) 的根節點 root, 找出在此 BST 中第 k 小的數.

時間複雜度要求為 O(n)
Constraints:

此 BST 至少存在一個 node
1 <= k <= number of total nodes in the BST
Example:

Input: k = 4, binary tree = 

    Level 0         5 (root)
                   / \
    Level 1       3   9
                 /   / \
    Level 2    -1   6   10
                     \
    Level 3           7

Output: 6
Explanation: 此 BST 的 node 由小至大排序為 [-1, 3, 5, 6, 7, 9, 10]，所以第 4 小的 node 為 6
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
    # @param k: int
    # @return int
    def findKthSmallestInBST(self, root, k):
        # Implement me
"""

