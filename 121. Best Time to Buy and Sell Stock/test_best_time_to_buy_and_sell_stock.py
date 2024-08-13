from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return profit


def test_1():
    prices = [7, 1, 5, 3, 6, 4]
    assert Solution().maxProfit(prices) == 5


def test_2():
    prices = [7, 6, 4, 3, 1]
    assert Solution().maxProfit(prices) == 0


def test_3():
    prices = [1]
    assert Solution().maxProfit(prices) == 0


def test_4():
    prices = [5, 1]
    assert Solution().maxProfit(prices) == 0


def test_5():
    prices = [2, 3]
    assert Solution().maxProfit(prices) == 1


def test_6():
    prices = [9, 7, 9, 1, 6, 4]
    assert Solution().maxProfit(prices) == 5
