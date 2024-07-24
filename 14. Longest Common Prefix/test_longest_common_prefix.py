from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:  # in case of no other strings are present
            return strs[0]

        shortest_string = ""
        shortest_string_length = 201
        for s in strs:
            if len(s) == 0:  # return if there is empty string
                return ""

            if len(s) < shortest_string_length:
                shortest_string = s
                shortest_string_length = len(s)

        common_string = []
        for i, l in enumerate(shortest_string):
            for s in strs:
                if s[i] != l:
                    return "".join(common_string)
            common_string.append(l)

        return "".join(common_string)


def test_1():
    strs = ["flower", "flow", "flight"]
    assert Solution().longestCommonPrefix(strs) == "fl"


def test_2():
    strs = ["dog", "racecar", "car"]
    assert Solution().longestCommonPrefix(strs) == ""


def test_3():
    strs = ["dog"]
    assert Solution().longestCommonPrefix(strs) == "dog"


def test_4():
    strs = ["dog", "", "dor"]
    assert Solution().longestCommonPrefix(strs) == ""


def test_5():
    strs = ["mehlikeli", "mehlik", "mehlimus"]
    assert Solution().longestCommonPrefix(strs) == "mehli"
