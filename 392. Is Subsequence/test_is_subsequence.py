class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:  # when s is empty, definetely substring
            return True

        # 2 pointers strategy
        i = j = 0
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                i += 1
            j += 1

        return i == len(s)


def test_1():
    s = "abc"
    t = "ahbgdc"
    assert Solution().isSubsequence(s, t)


def test_2():
    s = "axc"
    t = "ahbgdc"
    assert not Solution().isSubsequence(s, t)


def test_3():
    s = "gde"
    t = "gdblablae"
    assert Solution().isSubsequence(s, t)


def test_4():
    s = "ged"
    t = "gde"
    assert not Solution().isSubsequence(s, t)


def test_5():
    s = ""
    t = "abc"
    assert Solution().isSubsequence(s, t)


def test_6():
    s = "abc"
    t = ""
    assert not Solution().isSubsequence(s, t)
