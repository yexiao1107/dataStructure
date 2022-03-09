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
 

提示：

树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            cur_res = []
            cur_size = len(queue)
            for i in range(cur_size):
                cur_node = queue.pop(0)
                cur_res.append(cur_node.val)
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
            res.append(cur_res)
        return res
