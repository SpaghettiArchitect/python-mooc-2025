def main():
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    layers = int(input("Layers: "))
    sqr_size = layers * 2 - 1
    center = sqr_size // 2

    for row in range(sqr_size):
        for col in range(sqr_size):
            # Calculates distance to the center of the column and row
            abc_index = max(abs(col - center), abs(row - center))
            print(abc[abc_index], end="")
        print()


main()
