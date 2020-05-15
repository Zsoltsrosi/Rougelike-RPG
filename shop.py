import util
import inventory_sys
import skills
import random


def shop(level):
    util.clear_screen()
    welcome(level)
    display_shop(level)


def stat_calculator():
    ATTACK = skills.YOUR_STAT['attack'] - skills.BSIC_YOUR_STAT['attack']
    HP = skills.YOUR_STAT['health'] - skills.BSIC_YOUR_STAT['health']
    MANA = skills.YOUR_STAT['mana'] - skills.BSIC_YOUR_STAT['mana']
    Stat = [ATTACK, HP, MANA]
    return Stat


def items(level, item_type):
    item_fill = []
    item_stat = []
    i = 0
    while i != 5:
        rand = random.randint(0, 1)
        if rand == 1:
            get_loot_stat("weapon", level, item_stat)
            get_loot(1, item_fill)
        elif rand == 0:
            get_loot_stat("armor", level, item_stat)
            get_loot(2, item_fill)
        i += 1
    if item_type == "fill":
        return item_fill
    else:
        return item_stat


def get_loot_stat(loot, level, item_stat):
    if loot == "weapon":
        attack = (random.randint(1, 11)) + level
        stat = [0, 0, attack]
        item_stat.append(stat)
    elif loot == "armor":
        health = (random.randint(1, 11)) + level
        mana = (random.randint(1, 11)) + level
        stat = [health, mana, 0]
        item_stat.append(stat)


def get_loot(loot, item_fill):
    if loot == 1:
        name_1 = ["Sulivan's ", "broken ", "myne's "]
        name_2 = ["sword", "lance", "dagger"]
        part_1 = random.randint(0, 2)
        part_2 = random.randint(0, 2)
        word = name_1[part_1] + name_2[part_2]
        whole = [" ", word, " "]
        item_fill.append(whole)
    elif loot == 2:
        name_1 = ("Sulivan's ", "broken ", "myne's ")
        name_2 = ("cloak armor", "armor", "heavy armor")
        part_1 = random.randint(0, 2)
        part_2 = random.randint(0, 2)
        word = name_1[part_1] + name_2[part_2]
        whole = [" ", word, " "]
        item_fill.append(whole)


def display_shop(level):
    item_fill = items(level, "fill")
    item_stat = items(level, "stat")
    item_fill[0][0] = "│"
    item_fill[0][2] = "│"
    i = 0
    while i != 1:
        util.clear_screen()
        stat_boost = stat_calculator()
        print("Akashi's shop")
        print("Gold: ", inventory_sys.YOUR_GOLD['gold'])
        print("Current equipement: ", inventory_sys.equiped[0], ", ", inventory_sys.equiped[1])
        print("Current equipement stat boost: HP: ", stat_boost[1], " MANA: ", stat_boost[2], " DMG:", stat_boost[0])
        print("__________________________________________________________________")
        x = 0
        for i in item_fill:
            if item_fill[x][1] != " ":
                print(*item_fill[x])
            x += 1
        print("__________________________________________________________________")
        x = get_XY("X", item_fill)
        price = get_price(x, item_stat)
        print(" HP: ", item_stat[x][0], " MANA: ", item_stat[x][1], " DMG: ", item_stat[x][2])
        print(" Buy for: ", price, "GOLD")
        i = skill_input(item_fill, price, item_stat)


def get_price(x, item_stat):
    price = item_stat[x][0] + item_stat[x][1] + item_stat[x][2]
    price = price * 10
    return price


def skill_input(skill_fill, price, item_stat):
    key_input = util.key_pressed()
    row = get_XY("X", skill_fill)
    last = skill_fill[row]
    if key_input == "w":
        if row == 0:
            pass
        else:
            word = [skill_fill[row]]
            word[0][0] = " "
            word[0][-1] = " "
            word = [skill_fill[row - 1]]
            word[0][0] = "│"
            word[0][-1] = "│"
    elif key_input == "s":
        if last == skill_fill[-1]:
            pass
        else:
            word = [skill_fill[row]]
            word[0][0] = " "
            word[0][-1] = " "
            word = [skill_fill[row + 1]]
            word[0][0] = "│"
            word[0][-1] = "│"
    elif key_input == "e":
        if price < inventory_sys.YOUR_GOLD['gold']:
            if skill_fill[row][1] != " ":
                skill_fill[row][0] = " "
                skill_fill[row][2] = " "
                inventory_sys.inventory_fill.append(skill_fill[row])
                inventory_sys.inventory_stat.append(item_stat[row])
                skill_fill[row] = [" ", " ", " "]
                skill_fill[0][0] = "│"
                skill_fill[0][2] = "│"
                inventory_sys.YOUR_GOLD['gold'] -= price
        else:
            pass
    elif key_input == "q":
        return 1


def get_XY(coordinate, skill_fill):
    X = -1
    Y = -1
    for row in skill_fill:
        X += 1
        Y = -1
        for col in row:
            Y += 1
            if col == "│":
                if coordinate == "X":
                    return X
                elif coordinate == "Y":
                    return Y


def welcome(level):
    print("welcome traveler in my shop. I am Akashi you can find my shops at every 5th level of the duongeon")
    print("I see you come a long way and somehow got to the ", level, "th level with you outdated gear")
    print("But don't worry as I sell the best gear in the whole duongeon")
    print("Do you want to buy something?")
    util.key_pressed()
