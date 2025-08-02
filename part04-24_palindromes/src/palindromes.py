# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def main() -> None:
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        print("that wasn't a palindrome")


def palindromes(word: str) -> bool:
    # True, only if the word is equal to itself when reversed
    return word == word[::-1]


main()

if __name__ == "__main__":
    print(palindromes("python"))  # False
    print(palindromes("neveroddoreven"))  # True
