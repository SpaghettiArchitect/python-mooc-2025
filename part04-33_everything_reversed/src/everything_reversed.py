def everything_reversed(list_of_words: list[str]) -> list[str]:
    reversed_list = list_of_words[::-1]
    final_list = []
    for word in reversed_list:
        final_list.append(word[::-1])
    return final_list


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)  # ['erom eno', 'elpmaxe', 'ereht', 'iH']
