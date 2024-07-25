from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:  # handle easiest case
            return []

        ranges = []
        last = nums[0]  # assign last to the first elem
        for i in range(len(nums) - 1):  # iterate by pairs of neighbour elems
            if nums[i + 1] - nums[i] > 1:
                range_str = f"{last}" if nums[i] - last == 0 else f"{last}->{nums[i]}"
                ranges.append(range_str)
                last = nums[i + 1]  # shift last to the beginning of new range

        # handle last interval
        range_str = f"{last}" if nums[-1] - last == 0 else f"{last}->{nums[-1]}"
        ranges.append(range_str)

        return ranges


def test_1():
    nums = [0, 1, 2, 4, 5, 7]
    assert Solution().summaryRanges(nums) == ["0->2", "4->5", "7"]


def test_2():
    nums = [0, 2, 3, 4, 6, 8, 9]
    assert Solution().summaryRanges(nums) == ["0", "2->4", "6", "8->9"]


def test_3():
    nums = []
    assert Solution().summaryRanges(nums) == []


def test_4():
    nums = [0]
    assert Solution().summaryRanges(nums) == ["0"]


def test_5():
    nums = [-1, 0, 1]
    assert Solution().summaryRanges(nums) == ["-1->1"]


def test_6():
    nums = [-5, -2, -1, 1]
    assert Solution().summaryRanges(nums) == ["-5", "-2->-1", "1"]


def test_7():
    nums = [-5, -3, -1, 1]
    assert Solution().summaryRanges(nums) == ["-5", "-3", "-1", "1"]


def test_8():
    nums = [-5, -4, 0, 1]
    assert Solution().summaryRanges(nums) == ["-5->-4", "0->1"]
