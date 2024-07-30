from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while numbers[i] + numbers[j] != target:
            # we are guranteed to have target as a sum, so
            # move start to right when sum is less than target and end to left when otherwise
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

        return [i + 1, j + 1]


def test_1():
    numbers = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(numbers, target) == [1, 2]


def test_2():
    numbers = [2, 3, 4]
    target = 6
    assert Solution().twoSum(numbers, target) == [1, 3]


def test_3():
    numbers = [-1, 0]
    target = -1
    assert Solution().twoSum(numbers, target) == [1, 2]


def test_4():
    numbers = [-2, 0, 1, 2, 3]
    target = 0
    assert Solution().twoSum(numbers, target) == [1, 4]


def test_5():
    numbers = [-2, 0, 0, 1, 3]
    target = 0
    assert Solution().twoSum(numbers, target) == [2, 3]
