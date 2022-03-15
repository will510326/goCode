'''
這道題目曾出現在 Uber 的面試中。

給定一個 linked list 的 head node, 刪除所有總和為 0 的 sub linked lists, 直到此 linked list 不存在一個總和為 0 的 sub linked list 為止, 最後 return 刪除後的 linked list head node。

Example 1:

Input: 3 -> 2 -> 1 -> -1 -> -2 -> None
Output: 3 -> None
Explanation: Sub list 2 -> 1 -> -1 -> -2 的總和為 0, 所以可把此 sub list 刪除
Example 2:

Input: -5 -> 2 -> 1 -> -3 -> 10 -> 1 -> 2 -> -2 -> None
Output -5 -> 10 -> 1 -> None
Explanation: Sub lists 2 -> 1 -> -3 及 2 -> -2 各自的總和為 0, 所以可把這兩個 sub lists 刪除
Function Signature
# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    # @param head: ListNode
    # @retrun ListNode
    def removeZeroSumSublists(self, head):
        # Implement me
'''