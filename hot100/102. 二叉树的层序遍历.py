'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            length = len(queue)
            tmp = []
            for i in range(length):
                cur_node = queue.pop(0)
                tmp.append(cur_node.val)
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
            res.append(tmp)
        return res