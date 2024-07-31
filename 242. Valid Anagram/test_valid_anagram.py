from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def test_1():
    s = "anagram"
    t = "nagaram"
    assert Solution().isAnagram(s, t)


def test_2():
    s = "rat"
    t = "car"
    assert not Solution().isAnagram(s, t)


def test_3():
    s = "blabla"
    t = "albalb"
    assert Solution().isAnagram(s, t)


def test_4():
    s = "hi"
    t = "il"
    assert not Solution().isAnagram(s, t)


def test_5():
    s = "house"
    t = "oushm"
    assert not Solution().isAnagram(s, t)


def test_6():
    s = "a"
    t = "ab"
    assert not Solution().isAnagram(s, t)


def test_7():
    s = "ab"
    t = "a"
    assert not Solution().isAnagram(s, t)
