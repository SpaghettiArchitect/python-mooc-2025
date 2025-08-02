def row_correct(sudoku: list[list[int]], row_no: int) -> bool:
    row = sudoku[row_no]

    for num in range(1, 10):
        repetitions = 0
        for cell in row:
            if num == cell:
                repetitions += 1

        if repetitions > 1:  # row contains more than one of num
            return False

    return True


def column_correct(sudoku: list[list[int]], column_no: int) -> bool:
    for num in range(1, 10):
        repetitions = 0
        for row in sudoku:
            if num == row[column_no]:
                repetitions += 1
        if repetitions > 1:
            return False

    return True


def block_correct(sudoku: list[list[int]], row_no: int, column_no: int) -> bool:
    for num in range(1, 10):
        repetitions = 0
        for row in range(row_no, row_no + 3):
            for column in range(column_no, column_no + 3):
                if num == sudoku[row][column]:
                    repetitions += 1

        if repetitions > 1:
            return False

    return True


def sudoku_grid_correct(sudoku: list[list[int]]) -> bool:
    total_rows = len(sudoku)
    total_columns = len(sudoku[0])

    for row in range(total_rows):

        for column in range(total_columns):
            if (row % 3) == 0 and (column % 3 == 0):
                if not (block_correct(sudoku, row, column)):
                    return False
            else:
                if not (column_correct(sudoku, column)):
                    return False

        if not (row_correct(sudoku, row)):
            return False

    return True


if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(sudoku_grid_correct(sudoku1))  # False

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(sudoku_grid_correct(sudoku2))  # True
