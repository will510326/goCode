'''
這道題目曾出現在 ByteDance 的面試中。

給定一個 linked list 的 head node，刪除從後面數來第 k 個 node，最後 return 刪除後的 linked list 的 head node。

請在 one pass 以內達成目標 (one pass 的意思是最多只 traverse linked list 一遍)
若 k > linked list 長度，return 原 linked list 的 head node 即可
Constraints:

k >= 1
Example 1:

Input: linked list = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: linked list = 1 -> 2 -> 3 -> 5
Explanation: 從後數來第 2 個 node 為 node 4，所以刪除後為 1 -> 2 -> 3 -> 5
Example 2:

Input: linked list = 1 -> 2 -> 3 -> 4 -> 5, k = 5
Output: linked list = 2 -> 3 -> 4 -> 5
Explanation: 從後數來第 5 個 node 為 node 1，所以刪除後為 2 -> 3 -> 4 -> 5
Example 3:

Input: linked list = 1 -> 2 -> 3 -> 4 -> 5, k = 100
Output: linked list = 1 -> 2 -> 3 -> 4 -> 5
Explanation: k > linked list 的長度，所以 return 原 linked list 即可
Function Signature
# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    # @param head: ListNode
    # @param k: int
    # @return ListNode
    def removeKthNodeFromBehind(self, head, k):
        # Implement me
        
'''