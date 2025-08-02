def formatted(decimals: list[float]) -> list[str]:
    new_decimals = []
    for decimal in decimals:
        new_decimals.append(f"{decimal:.2f}")
    return new_decimals


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)  # ['1.23', '0.33', '0.11', '3.45']
