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
