import zeeslagje.zeeslagje as zeeslagje
import pytest


def test_board_returns_not_none():
    board = zeeslagje.Board()

    assert board is not None


def test_board_is_initialized():
    for row in zeeslagje.Board().board:
        assert all(space == 0 for space in row)


@pytest.mark.parametrize("size", [
    0, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
])
def test_board_is_square_and_size(size):
    board = zeeslagje.Board(size)
    assert len(board.board) == size
    assert all(len(row) == size for row in board.board)


def test_when_board_is_initialized_as_zeroes_bomb_returns_zero():
    board = zeeslagje.Board()
    row_count = 0
    for row in board.board:
        col_count = 0
        for col in row:
            assert board.bomb(row=row_count, col=col_count) is 0
            col_count += 1
        row_count += 1


def test_ship_is_recognised_on_board():
    bomb = False
    board = zeeslagje.Board()
    board.board[0][0] = 1
    row_count = 0
    for row in board.board:
        col_count = 0
        for col in row:
            if board.bomb(row=row_count, col=col_count) != 0:
                bomb = True
            col_count += 1
        row_count += 1

    assert bomb is True
