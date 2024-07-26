from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index, end_index = 0, len(nums) - 1

        # corner cases
        if target <= nums[start_index]:
            return start_index
        if target > nums[end_index]:
            return end_index + 1
        if start_index == end_index:
            return start_index

        # main binary search
        while end_index - start_index > 1:
            middle_index = start_index + (end_index - start_index) // 2

            if target > nums[middle_index]:  # shift search range to right
                start_index = middle_index
            elif target < nums[middle_index]:  # shift search range to left
                end_index = middle_index
            else:
                # find exact location when target equal mid index elem
                return middle_index

        return start_index + 1


def test_1():
    nums = [1, 3, 5, 6]
    target = 5
    assert Solution().searchInsert(nums, target) == 2


def test_2():
    nums = [1, 3, 5, 6]
    target = 2
    assert Solution().searchInsert(nums, target) == 1


def test_3():
    nums = [1, 3, 5, 6]
    target = 7
    assert Solution().searchInsert(nums, target) == 4


def test_4():
    nums = [1, 3, 5, 6]
    target = -2
    assert Solution().searchInsert(nums, target) == 0


def test_5():
    nums = [1, 3, 5, 6]
    target = 4
    assert Solution().searchInsert(nums, target) == 2


def test_6():
    nums = [1]
    target = 1
    assert Solution().searchInsert(nums, target) == 0


def test_7():
    nums = [0]
    target = 1
    assert Solution().searchInsert(nums, target) == 1


def test_8():
    nums = [1, 3]
    target = 2
    assert Solution().searchInsert(nums, target) == 1


def test_9():
    nums = [1, 2]
    target = 3
    assert Solution().searchInsert(nums, target) == 2


def test_10():
    nums = [1, 2, 3]
    target = 2
    assert Solution().searchInsert(nums, target) == 1


def test_11():
    nums = [1, 3]
    target = 1
    assert Solution().searchInsert(nums, target) == 0
