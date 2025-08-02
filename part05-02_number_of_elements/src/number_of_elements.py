def count_matching_elements(my_matrix: list[list[int]], element: int):
    total_matches = 0
    for row in my_matrix:
        for column in row:
            if column == element:
                total_matches += 1

    return total_matches


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
