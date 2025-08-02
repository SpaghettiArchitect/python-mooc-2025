from fractions import Fraction


def main() -> None:
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))


def fractionate(amount: int) -> list[Fraction]:
    result = []
    for _ in range(amount):
        result.append(Fraction(1, amount))

    return result


# main()
