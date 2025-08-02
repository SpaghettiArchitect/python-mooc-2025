from random import choice, randint


def main() -> None:
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)


def roll(die: str) -> int:
    die_sides = []
    if die == "A":
        die_sides = [3, 3, 3, 3, 3, 6]
    elif die == "B":
        die_sides = [2, 2, 2, 5, 5, 5]
    elif die == "C":
        die_sides = [1, 4, 4, 4, 4, 4]

    i = randint(0, len(die_sides) - 1)

    return die_sides[i]


def play(die1: str, die2: str, times: int) -> tuple[int, int, int]:
    wins_die1 = 0
    wins_die2 = 0
    draws = 0
    for _ in range(times):
        result_die1 = roll(die1)
        result_die2 = roll(die2)
        if result_die1 > result_die2:
            wins_die1 += 1
        elif result_die2 > result_die1:
            wins_die2 += 1
        else:
            draws += 1

    return wins_die1, wins_die2, draws


# main()
