#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return head
        small = ListNode(-101)
        res1 = small
        big = ListNode(-101)
        res2 = big
        cur = head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            cur = cur.next
        big.next = None
        small.next = res2.next
        return res1.next

# @lc code=end

