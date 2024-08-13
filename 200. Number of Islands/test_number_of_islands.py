from typing import List


class Solution:
    def dfs(self, point: tuple) -> None:
        x, y = point

        # add to visited and replace land to water
        self.visited.add(point)
        self.grid[x][y] = "0"

        # calculate all real neighbours
        neighbours = [
            p
            for p in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            if (0 <= p[0] < self.n)  #  rows borders
            and (0 <= p[1] < self.m)  # cols borders
            and (self.grid[p[0]][p[1]] == "1")  # only land
            and (p not in self.visited)  # only if not visited
        ]

        # dfs real neighbours
        for neighbour in neighbours:
            self.dfs(neighbour)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.n, self.m = len(grid), len(grid[0])
        self.visited: set[tuple] = set()
        self.grid = grid

        # iterating by each cell, skipping if land is not found
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] != "1":
                    continue

                point = (i, j)
                if point not in self.visited:
                    self.dfs(point)
                    count += 1

        return count


def test_1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert Solution().numIslands(grid) == 1


def test_2():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert Solution().numIslands(grid) == 3


def test_3():
    grid = [
        ["0", "0", "1", "1", "0"],
        ["1", "0", "0", "1", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "1"],
    ]
    assert Solution().numIslands(grid) == 5


def test_4():
    grid = [
        ["0", "1", "0", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "0"],
    ]
    assert Solution().numIslands(grid) == 3


def test_5():
    grid = [
        ["0", "1", "0", "1", "0"],
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
    ]
    assert Solution().numIslands(grid) == 7
