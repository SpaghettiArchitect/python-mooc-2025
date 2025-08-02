import math


def main() -> None:
    print(hypotenuse(3, 4))  # 5.0
    print(hypotenuse(5, 12))  # 13.0
    print(hypotenuse(1, 1))  # 1.4142135623730951


def hypotenuse(leg1: float, leg2: float):
    return math.sqrt(math.pow(leg1, 2) + math.pow(leg2, 2))


# main()
