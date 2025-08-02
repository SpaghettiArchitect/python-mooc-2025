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


if __name__ == "__main__":
    sudoku = [
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

    print(block_correct(sudoku, 0, 0))  # False
    print(block_correct(sudoku, 1, 2))  # True
