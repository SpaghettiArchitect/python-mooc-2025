# Write your solution here
def first_word(sentence):
    # first occurrence of <space> character
    first_space_index = sentence.find(" ")
    return sentence[0:first_space_index]


def second_word(sentence):
    first_space_index = sentence.find(" ")
    new_sentence = sentence[(first_space_index + 1) :]
    if new_sentence.find(" ") == -1:
        return sentence[first_space_index + 1 :]
    else:
        second_space_index = first_space_index + new_sentence.find(" ") + 1
        return sentence[first_space_index + 1 : second_space_index]


def last_word(sentence):
    # search the string in reverse order until it finds a <space> character
    i = -1
    while i > -len(sentence):
        if sentence[i] == " ":
            break
        i -= 1
    return sentence[i + 1 :]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
