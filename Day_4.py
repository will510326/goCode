"""
這道題目曾出現在 Amazon 的面試中。

將 k 個排序過的 linked list merge 成一個新的已排序的 linked list, 並 return merge 後的 linked list head node。Input 是長度為 k 的 array, 該 array 存放 k 個 linked list 的 head node。

時間複雜度要求為 O(nlogk), 其中 n 為 merge 後的 linked list 總長度
Constraints:

k >= 0
Example 1:

Input: lists = [5 -> 10, 1 -> 3 -> 5 -> 7, -1 -> 11, 0 -> 10 -> 20]
Output: -1 -> 0 -> 1 -> 3 -> 5 -> 5 -> 7 -> 10 -> 10 -> 11 -> 20
Example 2:

Input: lists = [-5, -10 -> 100, 9, None]
Output: -10 -> -5 -> 9 -> 100
Function Signature
# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    # @param lists: List[ListNode]
    # @return ListNode
    def mergeKSortedLists(self, lists):
        # Implement me
"""