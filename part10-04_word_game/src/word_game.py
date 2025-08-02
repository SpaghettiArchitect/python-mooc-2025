# Write your solution here
import random


class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) == len(player2_word):
            return None
        elif len(player1_word) > len(player2_word):
            return 1
        else:
            return 2


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        player1_vowels = self.__calc_vowels(player1_word)
        player2_vowels = self.__calc_vowels(player2_word)

        if player1_vowels > player2_vowels:
            return 1
        elif player2_vowels > player1_vowels:
            return 2
        else:
            return None

    def __calc_vowels(self, player_word: str) -> int:
        vowels = "aeiou"

        player_vowels = 0

        for char in player_word:
            if char in vowels:
                player_vowels += 1

        return player_vowels


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):

        possibilities = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        if player1_word not in possibilities and player2_word not in possibilities:
            return None

        if player1_word not in possibilities:
            return 2

        if player2_word not in possibilities:
            return 1

        if possibilities[player1_word] == player2_word:
            return 1
        elif possibilities[player2_word] == player1_word:
            return 2
        else:
            return None


if __name__ == "__main__":
    p = LongestWord(3)
    p.play()
