def times_ten(start_index: int, end_index: int):
    result = {}
    for value in range(start_index, end_index + 1):
        result[value] = value * 10

    return result


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)  # {3: 30, 4: 40, 5: 50, 6: 60}
