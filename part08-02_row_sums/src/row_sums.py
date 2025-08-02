def main() -> None:
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)


def row_sums(my_matrix: list):
    for row in my_matrix:
        total_row = sum(row)
        row.append(total_row)


if __name__ == "__main__":
    main()
