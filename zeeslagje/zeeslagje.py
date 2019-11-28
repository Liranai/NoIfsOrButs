from typing import List, Tuple


class Board:
    def __init__(self, size: int = 10):
        self.board: List[List[int]] = [[0] * size] * size

    def bomb(self, row, col):
        return self.board[row][col]


def add_ship(current_board: Board, ship_type: int, locations: List[Tuple[int, int]]):
    for x,y in locations:
        current_board.board[x][y] = ship_type

    return current_board
