import pytest

from python.A_Easy.A_Arrays.AAJ_ValidSudoku import valid_sudoku


def _board(rows: list[str]) -> list[list[str]]:
    """
    Convert a list of 9 strings (each length 9) into a 9x9 list-of-lists board.
    Use '.' for empty cells.
    """
    return [list(r) for r in rows]


CASES = [
    (
        "valid_board",
        _board([
            "53..7....",
            "6..195...",
            ".98....6.",
            "8...6...3",
            "4..8.3..1",
            "7...2...6",
            ".6....28.",
            "...419..5",
            "....8..79",
        ]),
        True,
    ),
    (
        "invalid_row_duplicate",
        _board([
            "53..7...5",
            "6..195...",
            ".98....6.",
            "8...6...3",
            "4..8.3..1",
            "7...2...6",
            ".6....28.",
            "...419..5",
            "....8..79",
        ]),
        False,
    ),
    (
        "invalid_col_duplicate",
        _board([
            "53..7....",
            "6..195...",
            ".98....6.",
            "8...6...3",
            "4..8.3..1",
            "7...2...6",
            ".6....28.",
            "...419..5",
            "....8..76",
        ]),
        False,
    ),
    (
        "invalid_subgrid_duplicate",
        _board([
            "53..7....",
            "6..195...",
            ".98....6.",
            "8...6...3",
            "4..8.3..1",
            "7...2...6",
            ".6....28.",
            "...419..5",
            "....8..73",
        ]),
        False,
    ),
]

@pytest.mark.parametrize("name, board, expected", CASES, ids=[c[0] for c in CASES])
def test_valid_sudoku(name: str, board: list[list[str]], expected: bool) -> None:
    assert valid_sudoku(board) is expected
