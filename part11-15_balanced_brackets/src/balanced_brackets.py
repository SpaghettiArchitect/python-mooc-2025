def balanced_brackets(my_string: str):
    new_str = "".join([char for char in my_string if char in "()[]"])

    if len(new_str) == 0:
        return True
    # There can't be just one bracket
    if len(new_str) == 1:
        return False

    # There should be exactly one opening bracket and one closing bracket
    if new_str.startswith("(") and not new_str.endswith(")"):
        return False
    elif new_str.startswith("[") and not new_str.endswith("]"):
        return False

    # remove first and last character
    return balanced_brackets(new_str[1:-1])


if __name__ == "__main__":
    ok = balanced_brackets("(((())))")
    print(ok)  # True

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok)  # False

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok)  # False

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok)  # False

    ok = balanced_brackets("([([])])")
    print(ok)  # True

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)  # True

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)  # False

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)  # False

    ok = balanced_brackets("(x)y)")
    print(ok)  # False
