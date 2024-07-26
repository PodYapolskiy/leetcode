from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = ListNode()
        pointer = head
        while list1 and list2:
            if list1.val <= list2.val:
                pointer.next = list1
                pointer = pointer.next
                list1 = list1.next
            else:
                pointer.next = list2
                pointer = pointer.next
                list2 = list2.next

        if list1:
            while list1:
                pointer.next = list1
                pointer = pointer.next
                list1 = list1.next

        if list2:
            while list2:
                pointer.next = list2
                pointer = pointer.next
                list2 = list2.next

        return head.next


def test_1():
    head = Solution().mergeTwoLists(
        ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))
    )

    values = []
    while head:
        values.append(head.val)
        head = head.next

    assert values == [1, 1, 2, 3, 4, 4]


def test_2():
    head = Solution().mergeTwoLists(None, None)

    values = []
    while head:
        values.append(head.val)
        head = head.next

    assert values == []


def test_3():
    head = Solution().mergeTwoLists(None, ListNode(0))

    values = []
    while head:
        values.append(head.val)
        head = head.next

    assert values == [0]


def test_4():
    head = Solution().mergeTwoLists(
        ListNode(1, ListNode(3, ListNode(5))), ListNode(2, ListNode(4, ListNode(6)))
    )

    values = []
    while head:
        values.append(head.val)
        head = head.next

    assert values == [1, 2, 3, 4, 5, 6]


def test_5():
    head = Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(3))

    values = []
    while head:
        values.append(head.val)
        head = head.next

    assert values == [1, 2, 3, 4]
