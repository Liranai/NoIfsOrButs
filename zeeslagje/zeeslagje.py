from typing import List, Tuple


class Board:
    def __init__(self, size: int = 10):
        self.board: List[List[int]] = [[0] * size] * size

    def bomb(self, row, col):
        return self.board[row][col]


def add_ship_vertically(current_board: Board, ship_type: int, start_location: Tuple[int, int]):
    row, col = start_location
    list_bla = [0] * ship_type
    locations = []

    for l in list_bla:
        locations.append((row, col))
        col += 1

    return add_ship(current_board=current_board, ship_type=ship_type, locations=locations)


def add_ship(current_board: Board, ship_type: int, locations: List[Tuple[int, int]]):
    for x, y in locations:
        current_board.board[x][y] = ship_type

    return current_board
