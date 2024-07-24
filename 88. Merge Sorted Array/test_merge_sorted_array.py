from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        # indexes of ends
        i, j = m - 1, n - 1

        k = 0
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[~k] = nums2[j]
                j -= 1
            else:
                nums1[~k] = nums1[i]
                i -= 1
            k += 1

        while j >= 0:
            nums1[~k] = nums2[j]
            j -= 1
            k += 1


merge =  Solution().merge


def test_1():
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 5, 6]
    merge(a, 3, b, 3)
    assert a == [1, 2, 2, 3, 5, 6]


def test_2():
    a = [1]
    b = []
    merge(a, 1, b, 0)
    assert a == [1]


def test_3():
    a = [0]
    b = [1]
    merge(a, 0, b, 1)
    assert a == [1]


def test_4():
    a = [5, 5, 0, 0]
    b = [1, 2]
    merge(a, 2, b, 2)
    assert a == [1, 2, 5, 5]


def test_5():
    a = [1, 3, 3, 0, 0]
    b = [2, 4]
    merge(a, 3, b, 2)
    assert a == [1, 2, 3, 3, 4]
