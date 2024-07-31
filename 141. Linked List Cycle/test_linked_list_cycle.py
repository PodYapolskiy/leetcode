from typing import Optional
import pytest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:  # 0 or 1 elems
            return False

        # fast and slow pointers strategy
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next  # moves 2 times faster
            slow = slow.next  # type: ignore

            # if cycle exists, fast pointer will eventually coincide with slow
            if fast == slow:
                return True

        return False

    def hasCycleOld(self, head: Optional[ListNode]) -> bool:
        visited = set()
        node = head
        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next

        return False


def test_1():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    assert Solution().hasCycle(head)


def test_2():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    assert Solution().hasCycle(head)


def test_3():
    head = ListNode(1)

    assert not Solution().hasCycle(head)


@pytest.mark.skip()
def test_4():
    head = ListNode(-1)
    head.next = ListNode(-2)
    head.next.next = ListNode(-3)
    head.next.next.next = ListNode(-4)

    assert Solution().hasCycle(head)


@pytest.mark.skip()
def test_5():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)

    assert Solution().hasCycle(head)
