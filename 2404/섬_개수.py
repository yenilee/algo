from icecream import ic


class Solution:
    def __init__(self, computers):
        self.computers = computers
        self.length = len(computers)
        self.answer = 0
        self.check_visited = [[False for _ in range(self.length)] for _ in range(self.length)]
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def check_near_by(self, row, column):
        self.check_visited[row][column] = True

        for index in range(3):
            next_row = row + self.dy[index]
            next_column = column + self.dx[index]
            if 0 <= next_row < self.length and 0 <= next_column < self.length:
                if self.computers[next_row][next_column] == 1 and self.check_visited[next_row][next_column] is False:
                    self.check_near_by(next_row, next_column)

    def get_answer(self, n):

        for i in range(n):
            for j in range(n):
                if not self.check_visited[i][j] and self.computers[i][j] == 1:
                    self.check_near_by(i, j)
                    self.answer += 1
        return self.answer


def solution(n, computers):
    return Solution(computers).get_answer(n)


ic(solution(4, [
    [1, 1, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 1, 1]]))

ic(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

ic(solution(5,

     [[1, 1, 0, 1, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 0, 1, 1, 1]]))
