from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a, b = Counter(ransomNote), Counter(magazine)

        for s in set(ransomNote):
            if a[s] > b[s]:
                return False

        return True


def test_1():
    ransomNote = "a"
    magazine = "b"
    assert not Solution().canConstruct(ransomNote, magazine)


def test_2():
    ransomNote = "aa"
    magazine = "ab"
    assert not Solution().canConstruct(ransomNote, magazine)


def test_3():
    ransomNote = "aa"
    magazine = "aab"
    assert Solution().canConstruct(ransomNote, magazine)


def test_4():
    ransomNote = "blabla"
    magazine = "blablabla"
    assert Solution().canConstruct(ransomNote, magazine)


def test_5():
    ransomNote = "blabla"
    magazine = "blablbl"
    assert not Solution().canConstruct(ransomNote, magazine)
