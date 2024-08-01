class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in range(len(s) - 1):
            sign = -1 if symbols[s[i]] < symbols[s[i + 1]] else 1
            answer += sign * symbols[s[i]]

        # add last symbol to the sum or return first if len == 1
        return answer + symbols[s[i + 1]] if len(s) > 1 else symbols[s[0]]


def test_1():
    s = "III"
    assert Solution().romanToInt(s) == 3


def test_2():
    s = "LVIII"
    assert Solution().romanToInt(s) == 58


def test_3():
    s = "MCMXCIV"
    assert Solution().romanToInt(s) == 1994


def test_4():
    s = "XLII"
    assert Solution().romanToInt(s) == 42


def test_5():
    s = "LXIX"
    assert Solution().romanToInt(s) == 69


def test_6():
    s = "D"
    assert Solution().romanToInt(s) == 500
