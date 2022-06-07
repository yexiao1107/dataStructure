'''
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def push_left(node):
            while node:
                stack.append(node)
                node = node.left
        stack = []
        visited = TreeNode(-1)
        res = []
        push_left(root)
        while stack:
            cur_node = stack[-1]
            if (cur_node.left == None or cur_node.left == visited) and cur_node.right != visited:
                res.append(cur_node.val)
                push_left(cur_node.right)
            if cur_node.right == None or cur_node.right == visited:
                visited = stack.pop()
        return res