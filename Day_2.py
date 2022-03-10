# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:29:38 2022

@author: WayneSWLiu
"""

"""
這道題目曾出現在 Facebook 的面試中。

給定一個 linked list 的 head node，將指定區間內的節點反轉，並 return 新 linked list 的 head node。

指定區間之定義為: 第 m 個 node 到第 n 個 node 所形成的 linked list
Time complexity 要求: One-pass O(N)
Constraints:

m and n are positive integers ==> m 和 n 是正整數
1 <= m < n <= length of the linked list
Example 1:

Input: Linked List = 6 -> 5 -> 4 -> 3 -> 2 -> 1, m = 2, n = 4
Output: 6 -> 3 -> 4 -> 5 -> 2 -> 1
Explanation: 將第二個 node 到第四個 node 所形成的 Linked List 反轉
Example 2:

Input: Linked List = 6 -> 5 -> 4 -> 3 -> 2 -> 1, m = 2, n = 6
Output: 6 -> 1 -> 2 -> 3 -> 4 -> 5
Explanation: 將第二個 node 到第六個 node 所形成的 Linked List 反轉
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        st = []
        left, node = None, head
        if m != 1:
            for i in range(1, m - 1):
                node = node.next
            left = node
            node = node.next # position m
        
        for i in range(m, n + 1):
            st.append(node)
            node = node.next
        
        l1, l2 = st.pop(), None
        if m == 1:
            head = l1
        else:
            left.next = l1
        
        while st:
            l2 = st.pop()
            l1.next = l2
            l1 = l2
        
        l1.next = node
        
        return head