class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        if h < n:
            return -1  # impossible case for any substring

        for i in range(0, h - n + 1):
            if haystack[i : i + n] == needle:  # check substrings
                return i

        return -1  # not found


def test_1():
    haystack = "sadbutsad"
    needle = "sad"
    assert Solution().strStr(haystack, needle) == 0


def test_2():
    haystack = "leetcode"
    needle = "leeto"
    assert Solution().strStr(haystack, needle) == -1


def test_3():
    haystack = "omghihiomghi"
    needle = "hi"
    assert Solution().strStr(haystack, needle) == 3


def test_4():
    haystack = "sabutsad"
    needle = "sad"
    assert Solution().strStr(haystack, needle) == 5


def test_5():
    haystack = "sbutad"
    needle = "sad"
    assert Solution().strStr(haystack, needle) == -1


def test_6():
    haystack = "mississippi"
    needle = "issip"
    assert Solution().strStr(haystack, needle) == 4
