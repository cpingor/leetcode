#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        sec = slow.next
        slow.next = None
        pre = None
        while sec:
            next = sec.next
            sec.next = pre
            pre = sec
            sec = next
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True
# @lc code=end

