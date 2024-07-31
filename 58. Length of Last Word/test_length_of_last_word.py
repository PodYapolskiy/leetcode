class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt, i = 0, len(s) - 1

        while s[i] == " ":  # shift pointer to first non space char from end
            i -= 1

        while i >= 0 and s[i] != " ":  # go until next space or start of string
            cnt += 1
            i -= 1

        return cnt


def test_1():
    s = "Hello World"
    assert Solution().lengthOfLastWord(s) == 5


def test_2():
    s = "   fly me   to   the moon  "
    assert Solution().lengthOfLastWord(s) == 4


def test_3():
    s = "luffy is still joyboy"
    assert Solution().lengthOfLastWord(s) == 6


def test_4():
    s = "Hell   "
    assert Solution().lengthOfLastWord(s) == 4


def test_5():
    s = "Hel"
    assert Solution().lengthOfLastWord(s) == 3
