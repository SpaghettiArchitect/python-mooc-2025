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


def add_number(sudoku: list[list[int]], row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number


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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
