from typing import List


class Solution:
    """O(1) mem solution requires reverse tricks
    1. ---->--> [convert_to] <--<----
    2. <--<---- [convert_to] --><----
    3. --><---- [convert_to] -->---->
    """

    def rotate(self, nums: List[int], k: int) -> None:
        n, k = len(nums), k % len(nums)

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


def test_1():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    Solution().rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_2():
    nums = [-1, -100, 3, 99]
    k = 2

    Solution().rotate(nums, k)
    assert nums == [3, 99, -1, -100]


def test_3():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 10

    Solution().rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_4():
    nums = [-1, -100, 3, 99]
    k = 0

    Solution().rotate(nums, k)
    assert nums == [-1, -100, 3, 99]


def test_5():
    nums = [-1, -100, 3, 99]
    k = 12

    Solution().rotate(nums, k)
    assert nums == [-1, -100, 3, 99]


def test_6():
    nums = [-1, -100, 3, 99]
    k = 3

    Solution().rotate(nums, k)
    assert nums == [-100, 3, 99, -1]
