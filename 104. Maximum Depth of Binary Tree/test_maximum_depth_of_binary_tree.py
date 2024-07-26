from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


def test_1():
    root = TreeNode(
        3,
        left=TreeNode(9),
        right=TreeNode(
            20,
            left=TreeNode(15),
            right=TreeNode(7)
        )
    )
    assert Solution().maxDepth(root) == 3     


def test_2():
    root = TreeNode(
        1,
        right=TreeNode(2)
    )
    assert Solution().maxDepth(root) == 2     
