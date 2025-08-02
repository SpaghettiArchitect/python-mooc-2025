# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):
    if len(string) == 0:
        print("*" * number)
    else:
        print(string[0] * number)


def triangle(size, char):
    i = 1
    while i <= size:
        line(i, char)
        i += 1


def box_of_hashes(width, height, char):
    row = 0
    while row < height:
        line(width, char)
        row += 1


def shape(size_t, char_t, rows_r, char_r):
    triangle(size_t, char_t)
    box_of_hashes(size_t, rows_r, char_r)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
