from typing import List


class Board:
    def __init__(self, size: int = 10):
        self.board: List[List[int]] = [[0] * size] * size
