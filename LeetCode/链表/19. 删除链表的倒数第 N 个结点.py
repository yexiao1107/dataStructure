'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dump = ListNode(-1)
        dump.next = head
        p1 = dump
        for i in range(n + 1): ##为啥是n+1?
            p1 = p1.next
        p2 = dump
        while p1:
            p2 = p2.next
            p1 = p1.next
        p2.next = p2.next.next
        return dump.next
