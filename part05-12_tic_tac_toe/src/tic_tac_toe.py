def play_turn(game_board: list, x: int, y: int, piece: str):
    if not (0 <= x <= 2 and 0 <= y <= 2):
        return False
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    return False


if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))  # True
    print(game_board)  # [['', '', 'X'], ['', '', ''], ['', '', '']]
