def print_sudoku(sudoku: list[list[int]]) -> None:
    grid_string = ""
    for row in range(len(sudoku)):
        current_row = ""
        for col in range(len(sudoku[row])):
            if col % 3 == 0:
                current_row += " "
            if sudoku[row][col] != 0:
                current_row += f"{sudoku[row][col]} "
            else:
                current_row += "_ "

        if row % 3 == 0:
            current_row = "\n" + current_row.strip() + "\n"
        else:
            current_row = current_row.strip() + "\n"
        grid_string += current_row

    print(grid_string.strip())


def copy_and_add(sudoku: list[list[int]], row_no: int, column_no: int, number: int):
    new_sudoku = []
    for row in sudoku:
        new_sudoku.append(row[:])
    new_sudoku[row_no][column_no] = number
    return new_sudoku


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
