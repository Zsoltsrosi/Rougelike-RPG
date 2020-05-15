import time
import util
board = [["_", "_", "_", "_", "_", "_", "_", "_", "_"],
         ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
         ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
         ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
         ["│", " ", " ", " ", " ", " ", " ", "I", "│"],
         ["│", " ", " ", " ", " ", " ", " ", " ", "O"],
         ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
         ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
         ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
         ["│", " ", " ", "E", " ", " ", "X", " ", "│"],
         ["⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻"]]


def get_XY(character):
    x = 0
    for row in board:
        y = 0
        for col in row:
            if col == character:
                return x, y
            y += 1
        x += 1
    return 0, 0


def counter():
    count = 0
    for row in board:
        for col in row:
            if col == "E":
                count += 1
    return count


def print_board():
    x = 0
    for i in board:
        print(*board[x])
        x += 1


def enemy_ai():
    x = 0
    for row in board:
        y = 0
        for col in row:
            if col == "E":
                ai_x, ai_y = x, y
                player_x, player_y = get_XY("X")
                dif_x = ai_x - player_x
                dif_y = player_y - ai_y
                print(x, y)
                time.sleep(2)
                if ai_x == 0 and ai_y == 0:
                    pass
                elif board[ai_x - 1][ai_y] == "X" or board[ai_x + 1][ai_y] == "X" or board[ai_x][ai_y + 1] == "X" or board[ai_x][ai_y - 1] == "X":
                    board[ai_x][ai_y] = " "
                    print("YOU LOST")
                    time.sleep(5)
                    continue
                elif dif_x > 0 and board[ai_x - 1][ai_y] == " ":
                    board[ai_x][ai_y] = " "
                    board[ai_x - 1][ai_y] = "M"
                    continue
                elif dif_x < 0 and board[ai_x + 1][ai_y] == " ":
                    board[ai_x][ai_y] = " "
                    board[ai_x + 1][ai_y] = "M"
                    continue
                else:
                    if dif_y > 0 and board[ai_x][ai_y + 1] == " ":
                        board[ai_x][ai_y] = " "
                        board[ai_x][ai_y + 1] = "M"
                        continue
                    elif dif_y < 0 and board[ai_x][ai_y - 1] == " ":
                        board[ai_x][ai_y] = " "
                        board[ai_x][ai_y - 1] = "M"
                        continue
            y += 1
        x += 1
    x = 0
    for row in board:
        y = 0
        for col in row:
            if col == "M":
                board[x][y] = "E"
            y += 1
        x += 1


def main():
    while True:
        util.clear_screen()
        print_board()
        enemy_ai()
        time.sleep(1)


if __name__ == "__main__":
    main()
