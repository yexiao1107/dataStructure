'''
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
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
    def inorderTraversal(self, root: TreeNode) -> [int]:
        '''
        左根右
        :param root:
        :return:
        '''
        res = []
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)##左子树一直入栈，压到叶子结点后出栈
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res
