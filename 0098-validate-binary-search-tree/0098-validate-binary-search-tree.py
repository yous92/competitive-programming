# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Time complexity : o(n)
        # Space complexity : o(n)
        
        def validate(node, min, max):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            left = validate(node.left,min,node.val)
            right = validate(node.right, node.val,max)

            return left & right

        return validate(root,float('-inf'), float('inf'))
        
        