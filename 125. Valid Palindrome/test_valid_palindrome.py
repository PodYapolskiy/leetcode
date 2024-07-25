class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j, n = 0, len(s) - 1, len(s)
        while i < j:
            # find next alnum symbol from left
            while not s[i].isalnum() and i < j:
                i += 1
            # find next alnum symbol from right
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i] != s[j]:  # compare definetely alnum symbols
                return False
            i += 1
            j -= 1

        return True


def test_1():
    s = "A man, a plan, a canal: Panama"
    assert Solution().isPalindrome(s)


def test_2():
    s = "race a car"
    assert not Solution().isPalindrome(s)


def test_3():
    s = " "
    assert Solution().isPalindrome(s)


def test_4():
    s = "nig g n"
    assert not Solution().isPalindrome(s)


def test_5():
    s = "mashallah hallahsam"
    assert Solution().isPalindrome(s)
