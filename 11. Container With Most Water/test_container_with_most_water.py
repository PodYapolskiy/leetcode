from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, l, r = 0, 0, len(height) - 1

        while l < r:
            temp = (r - l) * min(height[l], height[r])
            if area < temp:
                area = temp

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area

    def oldMaxArea(self, height: List[int]) -> int:
        area, l, r = 0, 0, len(height) - 1

        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            l, r = (l + 1, r) if (height[l] < height[r]) else (l, r - 1)

        return area


def test_1():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert Solution().maxArea(height) == 49


def test_2():
    height = [1, 1]
    assert Solution().maxArea(height) == 1


def test_3():
    height = [5, 1, 7, 3, 2, 1, 8]
    assert Solution().maxArea(height) == 30


def test_4():
    height = [1, 2, 3, 2, 1, 2, 3, 2, 1]
    assert Solution().maxArea(height) == 12


def test_5():
    height = [3, 2, 1, 20, 1, 20, 1, 2, 3]
    assert Solution().maxArea(height) == 40
