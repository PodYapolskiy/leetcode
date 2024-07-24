"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k."""
import pytest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        n, i, j = len(nums), 0, len(nums) - 1

        while i < j:
            if nums[i] == val and nums[j] != val:  # replace cur i-th val with j-th non val elem
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[j] == val:  #  shift end pointer to find new non val element
                j -= 1
            elif nums[i] != val:  # shift start pointer to find new val elem to replace
                i += 1

        # cases when all are of val
        if nums[0] == val:
            nums = []
            return 0

        # count amount
        count = sum([1 for num in nums if num != val])
        nums = nums[:count]
        return count



def test_1():
    nums = [3, 2, 2, 3]
    val = 3
    assert Solution().removeElement(nums, val) == 2
    assert sorted(nums[:2]) == sorted([2, 2])


def test_2():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    assert Solution().removeElement(nums, val) == 5
    assert sorted(nums[:5]) == sorted([0,1,4,0,3])


def test_3():
    nums = []
    val = 0
    assert Solution().removeElement(nums, val) == 0
    assert sorted(nums) == sorted([])


# @pytest.mark.skip()
def test_4():
    nums = [5, 5, 5, 5]
    val = 5
    assert Solution().removeElement(nums, val) == 0
    assert sorted(nums[:0]) == sorted([])


def test_5():
    nums = [4, 5]
    val = 5
    assert Solution().removeElement(nums, val) == 1
    assert sorted(nums[:1]) == sorted([4])


def test_6():
    nums = [2, 2, 3]
    val = 2
    assert Solution().removeElement(nums, val) == 1
    assert sorted(nums[:1]) == sorted([3])
