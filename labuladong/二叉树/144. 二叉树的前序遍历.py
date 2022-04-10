'''
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> [int]:
        '''
        根左右
        :param root:
        :return:
        '''
        res = []
        stack = []
        node = root
        while node or stack:
            if node:
                res.append(node.val)
                stack.append(node.right)  ##右子树进栈，先进后出
                node = node.left
            else:
                node = stack.pop()
        return res

    def traverse(self, root):
        def pushLeft(p):
            '''
            左子树压栈到底
            '''
            while p:
                ##前序遍历的位置
                self.stack.append(p)
                p = p.left

        self.res = []
        self.stack = []
        visited = TreeNode(-1)##定义上一次遍历的子树根节点
        pushLeft(root)

        while self.stack:
            cur = self.stack[-1]
            if (cur.left == None or cur.left == visited) and cur.right != visited:
                ##中序遍历位置
                pushLeft(cur.right)
            if cur.right == None or cur.right==visited:
                ##后续遍历的位置
                visited = self.stack.pop()
        return self.res

