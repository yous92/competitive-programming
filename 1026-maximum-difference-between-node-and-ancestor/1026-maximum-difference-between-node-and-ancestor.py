# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            left_diff = helper(node.left, min_val, max_val)
            right_diff = helper(node.right, min_val, max_val)

            return max(left_diff, right_diff)

        return helper(root, root.val, root.val)
        