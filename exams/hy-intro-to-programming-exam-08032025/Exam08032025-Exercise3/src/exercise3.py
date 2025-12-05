from fractions import Fraction


def fraction_calculator(calculation: str):
    # Implements reduction of the fraction
    if calculation.count("/") == 1:
        return str(convert_to_fraction(calculation))

    frac1, sym, frac2 = calculation.strip().split(" ")
    frac1 = convert_to_fraction(frac1)
    frac2 = convert_to_fraction(frac2)

    result = ""
    # Implements sum of fractions
    if sym == "+":
        result = str(frac1 + frac2)
    # Implements subtraction of fractions
    elif sym == "-":
        result = str(frac1 - frac2)
    # Implements multiplication of fractions
    elif sym == "*":
        result = str(frac1 * frac2)

    return result


def convert_to_fraction(fraction: str):
    return Fraction(fraction)
