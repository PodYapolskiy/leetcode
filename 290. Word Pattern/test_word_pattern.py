class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Logic is to apply function to find first occurance of object in string or list.
        If occurances in any place would differ, it means that pattern is not followed.
        """
        words = s.split(" ")
        return len(pattern) == len(words) and list(map(pattern.find, pattern)) == list(
            map(words.index, words)
        )

    def wordPatternOld(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        word_map, pattern_map = dict(), dict()
        for i in range(len(pattern)):
            symb, word = pattern[i], words[i]

            # if both are apsent, make bijection pair
            if not pattern_map.get(symb) and not word_map.get(word):
                pattern_map[symb] = word
                word_map[word] = symb
            # if one exists, other should also present and bijection should keeps
            elif pattern_map.get(symb) != word or word_map.get(word) != symb:
                return False

        return True


def test_1():
    pattern = "abba"
    s = "dog cat cat dog"
    assert Solution().wordPattern(pattern, s)


def test_2():
    pattern = "abba"
    s = "dog cat cat fish"
    assert not Solution().wordPattern(pattern, s)


def test_3():
    pattern = "aaaa"
    s = "dog cat cat dog"
    assert not Solution().wordPattern(pattern, s)


def test_4():
    pattern = "ab"
    s = "dog cat"
    assert Solution().wordPattern(pattern, s)


def test_5():
    pattern = "ab"
    s = "dog dog"
    assert not Solution().wordPattern(pattern, s)


def test_6():
    pattern = "aa"
    s = "dog cat"
    assert not Solution().wordPattern(pattern, s)
