# Copy here code of line function from previous exercise
def line(number, string):
    if len(string) == 0:
        print("*" * number)
    else:
        print(string[0] * number)


def box_of_hashes(height):
    # You should call function line here with proper parameters
    row = 0
    while row < height:
        line(10, "#")
        row += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
