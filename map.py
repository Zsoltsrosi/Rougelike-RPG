import random
import util
import fight
import inventory_sys
import help
import menu
import shop
import time
import sys


def shop_map():
    board = [["_", "_", "_", "_", "_", "_", "_", "_", "_"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", " ", " ", " ", " ", " ", " ", "S", "│"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["O", "X", " ", " ", " ", " ", " ", " ", "O"],
             ["⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻"]]
    return board


def turorial_map():
    board = [["_", "_", "_", "_", "_", "_", "_", "_", "_"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", "X", " ", " ", " ", " ", " ", "E", "O"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["│", " ", " ", " ", " ", " ", " ", " ", "│"],
             ["⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻", "⎻"]]
    return board


def generate_board(level):
    size = random.randint(15, 20)
    num = size - 2
    door = random.randint(1, num)
    board = []
    playermid = size - 3
    top = ["_"] * num
    bottom = ["⎻"] * num
    middle = [" "] * num
    door_mid = [" "] * playermid

    for index in range(size):
        if index == door:
            board.append("." * size)
            board[index] = ["O", "X", *door_mid, "O"]
        elif index == 0:
            board.append("." * size)
            board[index] = ["_", *top, "_"]
        elif index == size - 1:
            board.append("." * size)
            board[index] = ["⎻", *bottom, "⎻"]
        elif index != door:
            board.append("." * size)
            board[index] = ["│", *middle, "│"]
    fill_board(board, size, door)
    return board


def fill_board(board, size, door):
    count = 0
    while count != 15:
        row = random.randint(1, size - 1)
        col = random.randint(1, size - 1)
        if row == door:
            pass
        elif board[row][col] == " ":
            board[row][col] = "I"
            count += 1
    count = 0
    while count != 5:
        row = random.randint(1, size - 1)
        col = random.randint(1, size - 1)
        if row == door:
            pass
        elif board[row][col] == " ":
            board[row][col] = "E"
            count += 1


def get_stats(level):
    if level == 0:
        level = "Tutorial"
    if level == 5 or level == 10 or level == 15:
        level = "Shop"
    if level == 20:
        level = "BOSS"
    HP = fight.your_stats("HP")
    MP = fight.your_stats("MP")
    damage = fight.your_stats("damage")
    gold = fight.your_stats("gold")
    stat = [["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["Dungeon:", level],
            ["   HP:", HP],
            ["   MP:", MP],
            ["  DMG:", damage],
            [" Gold:", gold],
            ["level:", inventory_sys.YOUR_LEVEL["level"]],
            [" "]]
    return stat


def map(board, level):
    util.clear_screen()
    stat = get_stats(level)
    s = 0
    i = 0
    for index in board:
        print(*board[i], *stat[s])
        i += 1
        if s != 7:
            s += 1
        else:
            s = 7
    print("I = inventory  H = help")


def get_input(board, level):
    move = util.key_pressed()
    row = playerindex_row(board)
    col = playerindex_col(board)
    if move == "d":
        if board[row][col + 1] == "O":
            return 1
        elif board[row][col + 1] == "E":
            fight.fight_sys(level)
            board[row][col] = " "
            board[row][col + 1] = "X"
        elif board[row][col + 1] == " ":
            board[row][col] = " "
            board[row][col + 1] = "X"
        elif board[row][col + 1] == "S":
            shop.shop(level)
    elif move == "a":
        if board[row][col - 1] == " ":
            board[row][col] = " "
            board[row][col - 1] = "X"
        elif board[row][col - 1] == "E":
            fight.fight_sys(level)
            board[row][col] = " "
            board[row][col - 1] = "X"
        elif board[row][col - 1] == "S":
            shop.shop(level)
    elif move == "s":
        if board[row + 1][col] == " ":
            board[row][col] = " "
            board[row + 1][col] = "X"
        elif board[row + 1][col] == "E":
            fight.fight_sys(level)
            board[row][col] = " "
            board[row + 1][col] = "X"
        elif board[row + 1][col] == "S":
            shop.shop(level)
    elif move == "w":
        if board[row - 1][col] == " ":
            board[row][col] = " "
            board[row - 1][col] = "X"
        elif board[row - 1][col] == "E":
            fight.fight_sys(level)
            board[row][col] = " "
            board[row - 1][col] = "X"
        elif board[row - 1][col] == "S":
            shop.shop(level)
    elif move == "h":
        help.help()
    elif move == "i":
        inventory_sys.inventory()
    elif move == "q":
        util.clear_screen()
        sys.exit()
    return 0


def playerindex_row(board):
    X = 0
    for row in board:
        for col in row:
            if col == "X":
                return X
        X += 1


def playerindex_col(board):
    Y = 0
    for row in board:
        for col in row:
            if col == "X":
                return Y
            else:
                Y += 1
        Y = 0


def get_XY(character, board):
    x = 0
    for row in board:
        y = 0
        for col in row:
            if col == character:
                return x, y
            y += 1
        x += 1
    return 0, 0


def enemy_move(board, level):
    if level == 0 or level == 20:
        return 0
    else:
        x = 0
        for row in board:
            y = 0
            for col in row:
                if col == "E":
                    ai_x, ai_y = x, y
                    player_x, player_y = get_XY("X", board)
                    dif_x = ai_x - player_x
                    dif_y = player_y - ai_y
                    if ai_x == 0 and ai_y == 0:
                        pass
                    elif board[ai_x - 1][ai_y] == "X" or board[ai_x + 1][ai_y] == "X" or board[ai_x][ai_y + 1] == "X" or board[ai_x][ai_y - 1] == "X":
                        caught()
                        board[ai_x][ai_y] = " "
                        fight.fight_sys(level)
                        pass
                    elif dif_x > 0 and board[ai_x - 1][ai_y] == " " and dif_x < 5 and dif_y > -5 and dif_y < 5:
                        board[ai_x][ai_y] = " "
                        board[ai_x - 1][ai_y] = "M"
                        pass
                    elif dif_x < 0 and board[ai_x + 1][ai_y] == " " and dif_x > -5 and dif_y > -5 and dif_y < 5:
                        board[ai_x][ai_y] = " "
                        board[ai_x + 1][ai_y] = "M"
                        pass
                    else:
                        if dif_y > 0 and board[ai_x][ai_y + 1] == " " and dif_y < 5 and dif_x > -5 and dif_x < 5:
                            board[ai_x][ai_y] = " "
                            board[ai_x][ai_y + 1] = "M"
                            pass
                        elif dif_y < 0 and board[ai_x][ai_y - 1] == " " and dif_y > -5 and dif_x > -5 and dif_x < 5:
                            board[ai_x][ai_y] = " "
                            board[ai_x][ai_y - 1] = "M"
                            pass
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


def caught():
    util.clear_screen()
    print("They caught you prepare for the fight")
    time.sleep(2)


def main():
    level = 0
    menu.main_menu()
    while level != 21:
        i = 0
        if level == 5 or level == 10 or level == 15:
            board = shop_map()
            map(board, level)
        elif level == 20:
            board = turorial_map()
            map(board, level)
        elif level > 0:
            board = generate_board(level)
            map(board, level)
        elif level == 0:
            board = turorial_map()
            map(board, level)
        while i != 1:
            i = get_input(board, level)
            map(board, level)
            enemy_move(board, level)
            map(board, level)
            if i == 1:
                level += 1
    win()


def win():
    util.clear_screen()
    help.logo("win")
    print("You beat the boss of the duongeon and are able to go back to your old life")
    print("Thank you for playing.")
    util.key_pressed()


if __name__ == "__main__":
    main()
