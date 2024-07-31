from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        assert len(nums) % 2

        single = 0
        for num in nums:
            single ^= num  # 2 elems will eliminate each other and single will remain

        return single


def test_1():
    nums = [2, 2, 1]
    assert Solution().singleNumber(nums) == 1


def test_2():
    nums = [4, 1, 2, 1, 2]
    assert Solution().singleNumber(nums) == 4


def test_3():
    nums = [1]
    assert Solution().singleNumber(nums) == 1


def test_4():
    nums = [0, 0, 1, -1, 1]
    assert Solution().singleNumber(nums) == -1


def test_5():
    nums = [-20, 10, 0, -20, 0]
    assert Solution().singleNumber(nums) == 10
