'''
這道題目曾出現在 Microsoft 的面試中。

判斷給定的 singly linked list 是否為回文 (palindrome)。

Empty list 是 palindrome
此 linked list 為 integer list
Time complexity 要求為 O(n)
Space complexity 要求為 O(1)
Example 1:

Input: Linked List = 1 -> 2 -> 3 -> 3 -> 2 -> 1
Output: True
Example 2:

Input: Linked List = 1 -> 2 -> 3 -> 2 -> 1
Output: True
Example 3:

Input: Linked List = 1 -> 2 -> 3
Output: False
Explanation: 此 linked list 的正向 sequence 和反向 sequence 不同，所以不是回文
Function Signature
# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    # @param head: ListNode
    # @return Bool
    def isListPalindromic(self, head):
        # Implement me
'''