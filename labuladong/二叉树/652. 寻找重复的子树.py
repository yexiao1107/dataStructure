'''
给定一棵二叉树 root，返回所有重复的子树。

对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

如果两棵树具有相同的结构和相同的结点值，则它们是重复的。

 

示例 1：



输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]
示例 2：



输入：root = [2,1,1]
输出：[[1]]
示例 3：



输入：root = [2,2,2,3,null,3,null]
输出：[[2,3],[3]]
 

提示：

树中的结点数在[1,10^4]范围内。
-200 <= Node.val <= 200
'''


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def travers(root):
            if root is None: return "#"
            left = travers(root.left)
            right = travers(root.right)
            subTree = "{},{},{}".format(root.val, left, right)
            freq = tree_map.get(subTree, 0)
            if freq == 1:
                res.append(root)
            freq += 1
            tree_map[subTree] = freq
            return subTree
        tree_map = {}
        res = []
        return res