import skills
import inventory_sys
import util
import sys


def logo():
    print('''
     _______ _    _ ______   __  __           ____________ 
    |__   __| |  | |  ____| |  \/  |   /\    |___  /  ____|
       | |  | |__| | |__    | \  / |  /  \      / /| |__   
       | |  |  __  |  __|   | |\/| | / /\ \    / / |  __|  
       | |  | |  | | |____  | |  | |/ ____ \  / /__| |____ 
       |_|  |_|  |_|______| |_|  |_/_/    \_\/_____|______|                                                 
                                                        ''')


def menu_print():
    chooice = 0
    menu = [["│", "Play", "│"], [" ", "Quit", " "]]
    while chooice == 0:
        util.clear_screen()
        logo()
        x = 0
        for i in menu:
            print(*menu[x])
            x += 1
        chooice = menu_inputs(menu)
        if chooice == 1:
            return 1
        elif chooice == 2:
            return 2


def menu_inputs(menu):
    key = util.key_pressed()
    if key == "w":
        menu[0] = ["│", "Play", "│"]
        menu[1] = [" ", "Quit", " "]
        return 0
    elif key == "s":
        menu[1] = ["│", "Quit", "│"]
        menu[0] = [" ", "Play", " "]
        return 0
    elif key == "e":
        if menu[0][0] == "│":
            return 1
        elif menu[1][0] == "│":
            return 2
    else:
        return 0


def main_menu():
    util.clear_screen()
    chooice = menu_print()
    if chooice == 1:
        character_creation()
    elif chooice == 2:
        sys.exit()


def character_creation():
    menu = [["│", "knight", "│"], [" ", "soldier", " "], [" ", "viking", " "], [" ", "mage", " "]]
    i = 0
    while i == 0:
        util.clear_screen()
        stat = get_stat(menu)
        print("Before you came here you were a: ")
        print(" ")
        print(*menu[0], *menu[1])
        print(*menu[2], *menu[3])
        print("________________________")
        print(stat)
        i = char_input(menu)


def get_stat(menu):
    x = get_x(menu)
    if x == 0:
        return "Knights have high HP in cost of MANA"
    elif x == 1:
        return "Common soldiers are mostly balanced in every way"
    elif x == 2:
        return "Vikings have high ATTACK in cost of MANA and HP"
    else:
        return "Mages have high MANA but bad at ATTACKing and have low HP"


def update_stats(menu):
    x = get_x(menu)
    if x == 0:
        skills.BSIC_YOUR_STAT['attack'] = 3
        skills.BSIC_YOUR_STAT['health'] = 25
        skills.BSIC_YOUR_STAT['mana'] = 10
        inventory_sys.inventory_fill[0] = ["│", "Knight Armor", "│"]
        inventory_sys.inventory_stat[0] = [5, 0, 0]
        inventory_sys.inventory_fill[1] = [" ", "Knight's sword", " "]
        inventory_sys.inventory_stat[1] = [0, 0, 2]
    elif x == 1:
        skills.BSIC_YOUR_STAT['attack'] = 4
        skills.BSIC_YOUR_STAT['health'] = 20
        skills.BSIC_YOUR_STAT['mana'] = 10
        inventory_sys.inventory_fill[0] = ["│", "Soldier's armor", "│"]
        inventory_sys.inventory_stat[0] = [3, 3, 0]
        inventory_sys.inventory_fill[1] = [" ", "Common spear", " "]
        inventory_sys.inventory_stat[1] = [0, 0, 5]
    elif x == 2:
        skills.BSIC_YOUR_STAT['attack'] = 5
        skills.BSIC_YOUR_STAT['health'] = 15
        skills.BSIC_YOUR_STAT['mana'] = 3
        inventory_sys.inventory_fill[0] = ["│", "Viking armor", "│"]
        inventory_sys.inventory_stat[0] = [1, 0, 0]
        inventory_sys.inventory_fill[1] = [" ", "Viking axe", " "]
        inventory_sys.inventory_stat[1] = [0, 0, 5]
    else:
        skills.BSIC_YOUR_STAT['attack'] = 1
        skills.BSIC_YOUR_STAT['health'] = 15
        skills.BSIC_YOUR_STAT['mana'] = 40
        inventory_sys.inventory_fill[0] = ["│", "Mage robe", "│"]
        inventory_sys.inventory_stat[0] = [2, 5, 0]
        inventory_sys.inventory_fill[1] = [" ", "Mage staff", " "]
        inventory_sys.inventory_stat[1] = [0, 10, 2]
    skills.start_stat()


def get_x(menu):
    x = 0
    for row in menu:
        for col in row:
            if col == "│":
                return x
        x += 1


def char_input(menu):
    x = get_x(menu)
    chooice = util.key_pressed()
    if chooice == "w":
        if menu[x] != menu[0] and menu[x] != menu[1]:
            menu[x][0] = " "
            menu[x][2] = " "
            menu[x - 2][0] = "│"
            menu[x - 2][2] = "│"
        return 0
    elif chooice == "s":
        if menu[x] != menu[2] and menu[x] != menu[3]:
            menu[x][0] = " "
            menu[x][2] = " "
            menu[x + 2][0] = "│"
            menu[x + 2][2] = "│"
        return 0
    elif chooice == "d":
        if menu[x] != menu[1] and menu[x] != menu[3]:
            menu[x][0] = " "
            menu[x][2] = " "
            menu[x + 1][0] = "│"
            menu[x + 1][2] = "│"
        return 0
    elif chooice == "a":
        if menu[x] != menu[2] and menu[x] != menu[0]:
            menu[x][0] = " "
            menu[x][2] = " "
            menu[x - 1][0] = "│"
            menu[x - 1][2] = "│"
        return 0
    elif chooice == "e":
        update_stats(menu)
        return 1
    else:
        return 0
