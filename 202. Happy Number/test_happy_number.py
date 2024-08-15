class Solution:
    def nextN(self, n: int) -> int:
        s = i = 0
        while n:
            s += (n % 10) ** 2
            i += 1
            n //= 10

        return s

    def isHappy(self, n: int) -> bool:
        mem = set()  # store to catch cycle

        while n != 1 and n not in mem:
            mem.add(n)
            n = self.nextN(n)

        return n == 1


def test_1():
    n = 19
    assert Solution().isHappy(n)


def test_2():
    n = 2
    assert not Solution().isHappy(n)


def test_3():
    n = 100
    assert Solution().isHappy(n)


def test_4():
    # 25 => 4 + 25 = 29 => 4 + 81 = 85 => 64 + 25 = 89 => 64 + 81 = 145 => 1 + 16 + 25 = 42 => 16 + 4 = 20 => 4 => 16 => 37 => 9 + 49 = 58 => 25 + 64 = 89
    n = 5
    assert not Solution().isHappy(n)


def test_5():
    n = 82
    assert Solution().isHappy(n)
