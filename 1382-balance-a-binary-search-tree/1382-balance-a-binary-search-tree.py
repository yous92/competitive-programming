# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorderTraversal(node):
            if not node:
                return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)

        sorted_nodes = inorderTraversal(root)
    

        def buildBalancedBST(nodes):
            if not nodes:
                return None
            mid = len(nodes) // 2
            root = TreeNode(nodes[mid])
            root.left = buildBalancedBST(nodes[:mid])
            root.right = buildBalancedBST(nodes[mid + 1:])
            return root

        return buildBalancedBST(sorted_nodes)