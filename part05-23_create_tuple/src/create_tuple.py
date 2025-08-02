def create_tuple(x: int, y: int, z: int) -> tuple:
    smallest = min(x, y, z)
    greatest = max(x, y, z)
    total = sum([x, y, z])
    return (smallest, greatest, total)


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
