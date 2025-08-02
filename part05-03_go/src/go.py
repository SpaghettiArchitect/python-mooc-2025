def who_won(game_board: list[list[int]]):
    total_player_one = 0
    total_player_two = 0
    for row in game_board:
        for column in row:
            if column == 1:
                total_player_one += 1
            elif column == 2:
                total_player_two += 1
            else:
                continue

    if total_player_one > total_player_two:
        return 1
    elif total_player_two > total_player_one:
        return 2
    else:
        return 0
