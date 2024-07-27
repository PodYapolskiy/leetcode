from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        memory = set()
        while i < len(nums):
            if nums[i] not in memory:
                memory.add(nums[i])
                i += 1
            else:
                nums.pop(i)
        return len(memory)


def test_1():
    nums = [1, 1, 2]
    answer = Solution().removeDuplicates(nums)
    assert answer == 2
    assert nums[:answer] == [1, 2]


def test_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    answer = Solution().removeDuplicates(nums)
    assert answer == 5
    assert nums[:answer] == [0, 1, 2, 3, 4]


def test_3():
    nums = [1, 1, 1]
    answer = Solution().removeDuplicates(nums)
    assert answer == 1
    assert nums[:answer] == [1]


def test_4():
    nums = [0]
    answer = Solution().removeDuplicates(nums)
    assert answer == 1
    assert nums[:answer] == [0]


def test_5():
    nums = [-1, -1, 1, 1, 2, 2]
    answer = Solution().removeDuplicates(nums)
    assert answer == 3
    assert nums[:answer] == [-1, 1, 2]
