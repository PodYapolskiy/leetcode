from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:  # if coincide, more probably the majority elem
                count += 1
            else:  # decrease, less probably
                count -= 1

        return candidate


def test_1():
    nums = [3, 2, 3]
    assert Solution().majorityElement(nums) == 3


def test_2():
    nums = [2, 2, 1, 1, 1, 2, 2]
    assert Solution().majorityElement(nums) == 2


def test_3():
    nums = [-10]
    assert Solution().majorityElement(nums) == -10


def test_4():
    nums = [1, 1, 2, 2, 2, 2, 3, 3, 4, 2, 2]
    assert Solution().majorityElement(nums) == 2


def test_5():
    nums = [-5, 10, 12, 10, -4, 3, 10, 10, 10]
    assert Solution().majorityElement(nums) == 10
