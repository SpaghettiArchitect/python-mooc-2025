def transpose(matrix: list[list[int]]) -> None:
    result = []
    for col in range(len(matrix)):

        tmp_row = []
        for row in range(len(matrix)):
            tmp_row.append(matrix[row][col])
        result.append(tmp_row)

    matrix[:] = result


if __name__ == "__main__":
    original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(original)
    print(original)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
