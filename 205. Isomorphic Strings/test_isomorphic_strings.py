class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_arr, t_arr = [0] * 256, [0] * 256

        for i in range(len(s)):
            if s_arr[ord(s[i])] != t_arr[ord(t[i])]:
                return False

            s_arr[ord(s[i])] = i + 1
            t_arr[ord(t[i])] = i + 1

        return True


def test_1():
    s = "egg"
    t = "add"
    assert Solution().isIsomorphic(s, t)


def test_2():
    s = "foo"
    t = "bar"
    assert not Solution().isIsomorphic(s, t)


def test_3():
    s = "paper"
    t = "title"
    assert Solution().isIsomorphic(s, t)


def test_4():
    s = "dalailama"
    t = "hilialidi"
    assert Solution().isIsomorphic(s, t)


def test_5():
    s = "doom"
    t = "moud"
    assert not Solution().isIsomorphic(s, t)


def test_6():
    s = "badc"
    t = "baba"
    assert not Solution().isIsomorphic(s, t)


def test_7():
    s = "bbbaaaba"
    t = "aaabbbba"
    assert not Solution().isIsomorphic(s, t)
