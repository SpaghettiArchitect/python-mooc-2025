def factorials(n: int) -> dict[int, int]:
    result = {}
    for number in range(1, n + 1):
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        result[number] = factorial

    return result


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])  # 1
    print(k[3])  # 6
    print(k[5])  # 120
