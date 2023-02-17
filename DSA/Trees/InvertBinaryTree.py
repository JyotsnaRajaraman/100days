# Question
# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(root):
        if root is None:
            return None
        node = TreeNode(root.val)
        node.left = self.invertTree(root.right)
        node.right = self.invertTree(root.left)

        return node
