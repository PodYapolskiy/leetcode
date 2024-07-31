from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if any node is None, check whether other is also None, base case
        if not p or not q:
            return p == q

        # when both are not None, return False if values are not equal
        if p.val != q.val:
            return False

        # propogate to subtrees, "and" condition enables to propogate any "False" if any appeared
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test_1():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().isSameTree(p, q)


def test_2():
    p = TreeNode(1, left=TreeNode(2))
    q = TreeNode(1, right=TreeNode(2))
    assert not Solution().isSameTree(p, q)


def test_3():
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert not Solution().isSameTree(p, q)


def test_4():
    p = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
    q = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
    assert Solution().isSameTree(p, q)


def test_5():
    p = None
    q = TreeNode(1)

    assert not Solution().isSameTree(p, q)
