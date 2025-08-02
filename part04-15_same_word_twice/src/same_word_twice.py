rwords = []
counter = 0
while True:
    word = input("Word: ")
    if word in words:
        print(f"You typed in {counter} different words")
        break
    else:
        words.append(word)
        counter += 1
