#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            if slow.next == fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next
        sec = slow.next
        slow.next = None
        pre = None
        cur = sec
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        sec = pre
        first = head
        while first and sec:
            a, b = first.next, sec.next
            first.next = sec
            sec.next = a
            first = a
            sec = b
        return head

# @lc code=end

