def filter_forbidden(string: str, forbidden: str):
    filter_string = [char for char in string if char not in forbidden]
    return "".join(filter_string)


if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)
