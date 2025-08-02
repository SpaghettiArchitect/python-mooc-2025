def is_neighbour(n1: int, n2: int) -> bool:
    """
    Returns True the difference of two numbers is 1.
    """
    return (n1 - n2 == 1) or (n1 - n2 == -1)


def longest_series_of_neighbours(numbers: list[int]) -> int:
    longest_neighbour = 1
    counter = 1
    i = 1
    for number in numbers:
        if i >= len(numbers):
            if counter > longest_neighbour:
                longest_neighbour = counter
            break
        next_number = numbers[i]
        if is_neighbour(number, next_number):
            counter += 1
        else:
            if counter > longest_neighbour:
                longest_neighbour = counter
                counter = 1
            else:
                counter = 1
        i += 1

    return longest_neighbour


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))  # 4
    my_list = [15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))  # 7
