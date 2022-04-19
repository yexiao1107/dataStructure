'''
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

 

示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序 排列
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dump = ListNode(-1, head)
        pre = dump
        cur = pre.next
        while cur:
            nxt = cur.next##当前节点下一个
            while nxt and nxt.val == cur.val:#下一个节点值和当前节点一样，一直跑到不一样位置
                nxt = nxt.next
            if nxt != cur.next:##如果下一个节点移动了，就把pre指针指向它，就跳过了不同的
                pre.next = nxt
                cur = nxt
            else:
                pre = cur
                cur = nxt
        return dump.next
