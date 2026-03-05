def valid_sudoku(board: list[list[int]]) -> bool:
    SIZE = 9
    rowMap = [ dict() for _ in range(SIZE) ]
    colMap = [ dict() for _ in range(SIZE) ]
    sqMap = [ dict() for _ in range(SIZE) ]

    for i in range(SIZE):
        for j in range(SIZE):
            val = board[i][j]
            if val == ".":
                continue

            # Rows Check
            if val in rowMap[i]:
                return False
            else:
                rowMap[i][val] = True

            # Cols Check
            if val in colMap[j]:
                return False
            else:
                colMap[j][val] = True

            # Squares Check
            sq = (i // 3) * 3 + (j // 3)
            if val in sqMap[sq]:
                return False
            else:
                sqMap[sq][val] = True
    
    return True
