from random import randint


class Dice:
    def __init__(self, sides: int = 6):
        self.__sides = sides

    def roll_dice(self, times: int):
        results = []
        for _ in range(times):
            results.append(randint(1, self.__sides))
        return results

    def __str__(self):
        return f"{self.__sides}-sided dice"


class DiceGame:
    def __init__(self, dice: Dice):
        self.__dice = dice

    def roll_once(self):
        # Rolls the dice 5 times.
        roll = self.__dice.roll_dice(5)
        if not self.__check_for_same_value(roll):
            str_roll = [str(num) for num in sorted(roll)]
            str_roll = ", ".join(str_roll)
            print(f"Rolled 5 dice and got {str_roll}.")
        else:
            print("Yatzy!")

    def __check_for_same_value(self, roll: list):
        first_num = roll[0]
        for current_num in roll:
            if current_num != first_num:
                return False
        else:
            return True

    def roll_five_of_a_kind(self):
        attempts = 0
        while True:
            current_roll = self.__dice.roll_dice(5)
            attempts += 1
            if self.__check_for_same_value(current_roll):
                break
        print(f"It took {attempts} rolls to get five of a kind.")

    def __str__(self):
        instructions = "The goal of the game is to roll the dice"
        instructions += " and get 5 of the same number."
        instructions += f" Using {self.__dice}."
        return instructions
