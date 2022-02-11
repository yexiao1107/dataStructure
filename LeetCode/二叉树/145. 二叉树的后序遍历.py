'''
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

 

示例 1：


输入：root = [1,null,2,3]
输出：[3,2,1]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
 

提示：

树中节点的数目在范围 [0, 100] 内
-100 <= Node.val <= 100
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> [int]:
        '''
        左右根，反转或头插法，但不是真正的后续遍历
        :param root:
        :return:
        '''
        res = []
        stack = []
        node = root
        while node or stack:
            if node:
                res.append(node.val)
                stack.append(node.left)  ##左子树全部压栈，后出，形成根右左，和前序遍历相反，输出时翻过来
                node = node.right
            else:
                node = stack.pop()
        return res[::-1]

    def postorderTraversalV2(self, root: TreeNode) -> [int]:
        '''
        左右根
        :param root:
        :return:
        '''
        res = []
        stack = []
        pre_node = None
        while root or stack:
            while root:
                stack.append(root)  ##左子树全部进栈
                root = root.left
            root = stack.pop()
            if root.right == None or root.right == pre_node:  ##访问条件，叶子结点或右子树被访问过，则该节点是根节点，这次访问
                res.append(root.val)
                pre_node = root
                root = None
            else:  ##非叶子结点或者右子树没被访问，弹出的根节点继续压回栈
                stack.append(root)
                root = root.right
        return res
