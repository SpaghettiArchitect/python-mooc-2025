from datetime import datetime


def main() -> None:
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))


def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False

    # A tuple, containing day, month, year and personal-id as strings
    date_str = (pic[:2], pic[2:4], pic[4:6], pic[7:-1])
    try:
        year = int(date_str[2])
        month = int(date_str[1])
        day = int(date_str[0])
        id = int(date_str[3])
    except ValueError:
        return False

    century_marker = pic[6]
    century = -1
    if century_marker in "+-A":
        if century_marker == "+":
            century = 1800
        elif century_marker == "-":
            century = 1900
        else:
            century = 2000
    else:
        return False

    year += century
    try:
        datetime(year, month, day)
    except ValueError:
        return False

    control_char = pic[-1]
    if control_char != calc_control_char(date_str):
        return False

    return True


def calc_control_char(digits: tuple[str, str, str, str]) -> str:
    all_control_char = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    nine_digit = ""
    for digit in digits:
        nine_digit += digit

    index = int(nine_digit) % 31

    return all_control_char[index]


# main()
