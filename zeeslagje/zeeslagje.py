from typing import List


class Board:
    def __init__(self, size: int = 10):
        self.board: List[List[int]] = [[0] * size] * size

    def bomb(self, row, col):
        return self.board[row][col]

