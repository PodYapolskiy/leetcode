class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        stack = []
        braces = {"(": ")", "[": "]", "{": "}"}
        for brace in s:
            if brace in ["(", "[", "{"]:
                stack.append(brace)
            else:
                if len(stack) == 0:
                    return False

                if braces[stack.pop()] != brace:
                    return False

        return len(stack) == 0


def test_1():
    s = "()"
    assert Solution().isValid(s)


def test_2():
    s = "()[]{}"
    assert Solution().isValid(s)


def test_3():
    s = "(]"
    assert not Solution().isValid(s)


def test_4():
    s = "([{}])"
    assert Solution().isValid(s)


def test_5():
    s = "({[}])"
    assert not Solution().isValid(s)


def test_6():
    s = "(("
    assert not Solution().isValid(s)
