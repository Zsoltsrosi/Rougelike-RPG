import util
import skills
import random

YOUR_GOLD = {"gold": 0}
YOUR_LEVEL = {"level": 0,
              "XP": 0,
              "count": 0}


def inventory():
    leveling()
    util.clear_screen()
    print_inventory()


def print_inventory():
    i = 0
    while i != 1:
        util.clear_screen()
        yourstat = stat_get()
        menu = ['│INVENTORY│', '                        ', ' SKILLS ']
        print(*menu)
        print('---------------------------------------------')
        index = 0
        print(*yourstat)
        print("Armor: ", equiped[0])
        print("Weapon: ", equiped[1])
        print('---------------------------------------------')
        for i in inventory_fill:
            print(*inventory_fill[index])
            index += 1
        i = inv_input()


def inv_input():
    key_input = util.key_pressed()
    row = get_XY("X")
    last = inventory_fill[row]
    if key_input == "w":
        if row == 0:
            pass
        else:
            word = [inventory_fill[row]]
            word[0][0] = " "
            word[0][-1] = " "
            word = [inventory_fill[row - 1]]
            word[0][0] = "│"
            word[0][-1] = "│"
    elif key_input == "s":
        if last == inventory_fill[-1]:
            pass
        else:
            word = [inventory_fill[row]]
            word[0][0] = " "
            word[0][-1] = " "
            word = [inventory_fill[row + 1]]
            word[0][0] = "│"
            word[0][-1] = "│"
    elif key_input == "d":
        skills.skill()
        return 1
    elif key_input == "e":
        if inventory_stat[row][2] == 0:
            equiped[0] = inventory_fill[row][1]
            stat_differ(row, 'armor')
        else:
            equiped[1] = inventory_fill[row][1]
            stat_differ(row, 'attack')
    elif key_input == "q":
        return 1


def stat_differ(row, stat_type):
    if stat_type == 'armor':
        skills.YOUR_STAT['health'] = skills.BSIC_YOUR_STAT['health'] + inventory_stat[row][0]
        skills.YOUR_STAT['mana'] = skills.BSIC_YOUR_STAT['mana'] + inventory_stat[row][1]
    else:
        skills.YOUR_STAT['attack'] = skills.BSIC_YOUR_STAT['attack'] + inventory_stat[row][2]


def get_XY(coordinate):
    X = -1
    Y = -1
    for row in inventory_fill:
        X += 1
        Y = -1
        for col in row:
            Y += 1
            if col == "│":
                if coordinate == "X":
                    return X
                elif coordinate == "Y":
                    return Y


def stat_get():
    row = get_XY("X")
    newhp = stat_calculator('HP')
    newmp = stat_calculator('MP')
    newdmg = stat_calculator('DMG')
    if newhp > -1:
        newhp = "+", newhp
        newhp = ' '.join([str(elem) for elem in newhp])
    if newmp > -1:
        newmp = "+", newmp
        newmp = ' '.join([str(elem) for elem in newmp])
    if newdmg > -1:
        newdmg = "+", newdmg
        newdmg = ' '.join([str(elem) for elem in newdmg])
    if inventory_stat[row][2] == 0:
        stat = ["HP:", skills.YOUR_STAT['health'], newhp,
                "  MP:", skills.YOUR_STAT['mana'], newmp,
                "  DMG:", skills.YOUR_STAT['attack'], "+ 0"]
        return stat
    else:
        stat = ["HP:", skills.YOUR_STAT['health'], "+ 0",
                "  MP:", skills.YOUR_STAT['mana'], "+ 0",
                "  DMG:", skills.YOUR_STAT['attack'], newdmg]
        return stat


def get_inv_stat(stat_type):
    X = -1
    Y = -1
    for row in inventory_fill:
        X += 1
        Y = -1
        for col in row:
            Y += 1
            if col == "│":
                if stat_type == "HP":
                    stat = inventory_stat[X][0]
                    return stat
                elif stat_type == "MP":
                    stat = inventory_stat[X][1]
                    return stat
                else:
                    stat = inventory_stat[X][2]
                    return stat


def fill_inventory(looted):
    if looted != " ":
        inventory_fill.append(looted)
    return inventory


def xp_calculator(level):
    if level == 0:
        return 1000
    elif level > 10:
        return 500
    elif level < 10:
        return 250


def looting_phase(level):
    gold = random.randint(10, 120)
    YOUR_LEVEL["XP"] += xp_calculator(level)
    levelup = leveling()
    YOUR_GOLD['gold'] += gold
    loot = random.randint(1, 3)
    if loot > 0:
        name = get_loot()
        print("You won and looted a", name[1], "and", gold, "gold")
        fill_inventory(name)
        if levelup == 0:
            print("You leveled up")
        else:
            pass
    else:
        print("You got ", gold, "gold")


def get_loot_stat(loot):
    if loot == "weapon":
        attack = (random.randint(1, 11)) + YOUR_LEVEL['level']
        stat = [0, 0, attack]
        return stat
    else:
        health = (random.randint(1, 11)) + YOUR_LEVEL['level']
        mana = (random.randint(1, 11))
        stat = [health, mana, 0]
        return stat


def get_loot():
    count = random.randint(1, 2)
    if count == 1:
        name_1 = ["Sulivan's ", "broken ", "myne's "]
        name_2 = ["sword", "lance", "dagger"]
        part_1 = random.randint(0, 2)
        part_2 = random.randint(0, 2)
        stat = get_loot_stat("weapon")
        inventory_stat.append(stat)
        word = name_1[part_1] + name_2[part_2]
        whole = [" ", word, " "]
        return whole
    elif count == 2:
        name_1 = ("Sulivan's ", "broken ", "myne's ")
        name_2 = ("cloak armor", "armor", "heavy armor")
        part_1 = random.randint(0, 2)
        part_2 = random.randint(0, 2)
        stat = get_loot_stat("armor")
        inventory_stat.append(stat)
        word = name_1[part_1] + name_2[part_2]
        whole = [" ", word, " "]
        return whole


def stat_calculator(stat):
    row = get_XY("X")
    if stat == 'HP':
        num = skills.return_stats('HP', 'NEW', inventory_stat[row][0])
        return num
    elif stat == 'MP':
        num = skills.return_stats('MP', 'NEW', inventory_stat[row][1])
        return num
    else:
        num = skills.return_stats('DMG', 'NEW', inventory_stat[row][2])
        return num


def gold():
    return YOUR_GOLD['gold']


def leveling():
    if YOUR_LEVEL["XP"] > 999:
        YOUR_LEVEL["level"] += 1
        YOUR_LEVEL["XP"] -= 1000
        return 0


equiped = ["NONE", "NONE"]
inventory_fill = [[" ", "base armor", " "], ["│", "base sword", "│"]]
inventory_stat = [[1, 0, 0], [0, 0, 1]]
