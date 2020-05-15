import fight
import util
import inventory_sys
BSIC_YOUR_STAT = {'attack': 1,
                  'health': 20,
                  'mana': 20}
YOUR_STAT = {'attack': 1,
             'health': 20,
             'mana': 20}


def start_stat():
    YOUR_STAT['attack'] = BSIC_YOUR_STAT['attack']
    YOUR_STAT['health'] = BSIC_YOUR_STAT['health']
    YOUR_STAT['mana'] = BSIC_YOUR_STAT['mana']


def skill():
    leveling_skills()
    util.clear_screen()
    print_skill(skill_fill)


def print_skill(skill_fill):
    i = 0
    while i != 1:
        util.clear_screen()
        menu = [' INVENTORY ', '                        ', '│SKILLS│']
        print(*menu)
        print('---------------------------------------------')
        print("ATTACK: ", attack_skill[0], ",", attack_skill[1], ",", attack_skill[2])
        print("MAGIC: ", magic_skill[0], ",", magic_skill[1], ",", magic_skill[2])
        print('---------------------------------------------')
        index = 0
        for i in skill_fill:
            print(*skill_fill[index])
            index += 1
        print('---------------------------------------------')
        x = get_XY("X")
        print('DMG:', skill_stat[x][0] + skill_stat[x][2] + YOUR_STAT['attack'], '       Mana usage:', skill_stat[x][1])
        i = skill_input(skill_fill)


def skill_input(skill_fill):
    key_input = util.key_pressed()
    row = get_XY("X")
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
    elif key_input == "a":
        inventory_sys.inventory()
        return 1
    elif key_input == "e":
        if skill_stat[row][0] != 0:
            if attack_skill[0] == " ":
                attack_skill[0] = skill_fill[row][1]
            elif attack_skill[1] == " ":
                attack_skill[1] = skill_fill[row][1]
            elif attack_skill[2] == " ":
                attack_skill[2] = skill_fill[row][1]
            else:
                pass
        elif skill_stat[row][2] != 0:
            if magic_skill[0] == " ":
                magic_skill[0] = skill_fill[row][1]
            elif magic_skill[1] == " ":
                magic_skill[1] = skill_fill[row][1]
            elif magic_skill[2] == " ":
                magic_skill[2] = skill_fill[row][1]
            else:
                pass
    elif key_input == "r":
        i = 0
        while i != 3:
            magic_skill[i] = " "
            attack_skill[i] = " "
            i += 1
    elif key_input == "q":
        if attack_skill[0] == " " or attack_skill[1] == " " or attack_skill[2] == " ":
            if magic_skill[0] == " " or magic_skill[1] == " " or magic_skill[2] == " ":
                for i in 0, 1, 2:
                    attack_skill[i] = skill_fill[i][1]
                    magic_skill[i] = skill_fill[i + 3][1]
        return 1


def get_XY(coordinate):
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


def return_stats(stat, position, dif):
    if position == 'fight':
        fight.YOUR_STAT['attack'] = YOUR_STAT['attack']
        fight.YOUR_STAT['health'] = YOUR_STAT['health']
        fight.YOUR_STAT['mana'] = YOUR_STAT['mana']
    elif stat == 'HP':
        new_stat = BSIC_YOUR_STAT['health'] + dif
        num = new_stat - YOUR_STAT['health']
        return num
    elif stat == 'MP':
        new_stat = BSIC_YOUR_STAT['mana'] + dif
        num = new_stat - YOUR_STAT['mana']
        return num
    elif stat == 'DMG':
        new_stat = BSIC_YOUR_STAT['attack'] + dif
        num = new_stat - YOUR_STAT['attack']
        return num


def return_skills(skill_type):
    if skill_type == "attack":
        if attack_skill[0] == " ":
            attack = ["basic attack", " ", " "]
            return attack
        else:
            return attack_skill
    elif skill_type == "magic":
        if magic_skill[0] == " ":
            magic = ["Basic magic", "none", "none"]
            return magic
        else:
            return magic_skill
    elif skill_type == "inventory":
        inventory = ["small hp potion", "small mana potion", "bomb"]
        return inventory


def enemy_stats(stat_type, level):
    if stat_type == 'health':
        enemy_health = 20 + level + inventory_sys.YOUR_LEVEL['level']
        return enemy_health
    elif stat_type == 'attack':
        enemy_attack = 3 + level + inventory_sys.YOUR_LEVEL['level']
        return enemy_attack


def leveling_skills():
    level = inventory_sys.YOUR_LEVEL["level"]
    count = inventory_sys.YOUR_LEVEL["count"]
    if level == 1 and count == 0:
        skill_fill.append([" ", "forced thrust", " "])
        skill_stat.append([8, 3, 0])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 2 and count == 1:
        skill_fill.append([" ", "heavy slash", " "])
        skill_stat.append([9, 0, 0])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 3 and count == 2:
        skill_fill.append([" ", "water beam", " "])
        skill_stat.append([0, 10, 15])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 4 and count == 3:
        skill_fill.append([" ", "lava spit", " "])
        skill_stat.append([0, 5, 10])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 5 and count == 4:
        skill_fill.append([" ", "poisoned slash", " "])
        skill_stat.append([8, 0, 0])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 6 and count == 5:
        skill_fill.append([" ", "divine protection", " "])
        skill_stat.append([0, 5, 10])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 7 and count == 6:
        skill_fill.append([" ", "hidden blade", " "])
        skill_stat.append([10, 0, 0])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 8 and count == 7:
        skill_fill.append([" ", "summon beast", " "])
        skill_stat.append([0, 20, 20])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 9 and count == 8:
        skill_fill.append([" ", "divine slash", " "])
        skill_stat.append([15, 5, 0])
        inventory_sys.YOUR_LEVEL["count"] += 1
    elif level == 10 and count == 9:
        skill_fill.append([" ", "destroy", " "])
        skill_stat.append([50, 25, 0])
        inventory_sys.YOUR_LEVEL["count"] += 1


def return_hit(skill, dmg_type):
    if dmg_type == "attack":
        name = attack_skill[skill]
    else:
        name = magic_skill[skill]
    row = name_search(name)
    if fight.YOUR_STAT['mana'] > skill_stat[row][1]:
        fight.YOUR_STAT['mana'] -= skill_stat[row][1]
        fight.ENEMY_STAT['health'] -= skill_stat[row][0] + skill_stat[row][2] + YOUR_STAT['attack']
    else:
        fight.ENEMY_STAT['health'] -= 1
        fight.YOUR_STAT['mana'] += 5


def name_search(name):
    x = 0
    for row in skill_fill:
        for col in row:
            if col == name:
                return x
        x += 1


attack_skill = ["slash", "thrust", "whirlwind"]
magic_skill = ["fireball", "water arrow", "bless"]
skill_fill = [["│", "slash", "│"], [" ", "thrust", " "], [" ", "whirlwind", " "],
              [" ", "fireball", " "], [" ", "water arrow", " "], [" ", "bless", " "]]
skill_stat = [[1, 0, 0], [2, 0, 0], [4, 2, 0], [0, 5, 5], [0, 1, 3], [0, 3, 3]]
