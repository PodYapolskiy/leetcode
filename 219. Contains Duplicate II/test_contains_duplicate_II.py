from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in mem and i - mem[num] <= k:  # should exist, be close
                return True
            mem[num] = i  # update last index

        return False


def test_1():
    nums = [1, 2, 3, 1]
    k = 3
    assert Solution().containsNearbyDuplicate(nums, k)


def test_2():
    nums = [1, 0, 1, 1]
    k = 1
    assert Solution().containsNearbyDuplicate(nums, k)


def test_3():
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    assert not Solution().containsNearbyDuplicate(nums, k)


def test_4():
    nums = [1, 0]
    k = 1
    assert not Solution().containsNearbyDuplicate(nums, k)


def test_5():
    nums = [1, 2, 3, 1, 0, 1]
    k = 2
    assert Solution().containsNearbyDuplicate(nums, k)
