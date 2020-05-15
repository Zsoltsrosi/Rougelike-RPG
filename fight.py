import time
import util
import skills
import random
import inventory_sys
import help
import sys


YOUR_STAT = {'attack': 1,
             'health': 20,
             'mana': 20}
ENEMY_STAT = {'attack': 5,
              'health': 20,
              'og_health': 0}


def your_stats(stat):
    skills.return_stats('0', 'fight', '0')
    if stat == 'HP':
        return YOUR_STAT['health']
    elif stat == "MP":
        return YOUR_STAT['mana']
    elif stat == 'damage':
        return YOUR_STAT['attack']
    elif stat == 'gold':
        return inventory_sys.gold()


def enemy_stats(level):
    ENEMY_STAT['attack'] = skills.enemy_stats('attack', level)
    ENEMY_STAT['health'] = skills.enemy_stats('health', level)
    ENEMY_STAT['og_health'] = skills.enemy_stats('health', level)


def fight_sys(level):
    skills.return_stats('0', 'fight', '0')
    enemy_stats(level)
    og_health = YOUR_STAT['health']
    og_mana = YOUR_STAT['mana']
    if YOUR_STAT['health'] > 0 and ENEMY_STAT['health'] > 0:
        lose = fight(level)
        if lose == 2:
            util.clear_screen()
            inventory_sys.looting_phase(level)
            YOUR_STAT['health'] = og_health
            YOUR_STAT['mana'] = og_mana
            time.sleep(3)
        else:
            util.clear_screen()
            help.logo("lose")
            print("you lost the game for now but don't worry you can try again anytime. Good luck next time")
            print("Press any key to quit")
            util.key_pressed()
            sys.exit()


def get_name(level):
    if level == 0:
        return "Gate guard"
    elif level > 0 and level < 5:
        return "Crawler"
    elif level > 5 and level < 10:
        return "Undead soldier"
    elif level > 10 and level < 15:
        return "Abomination"
    elif level > 15 and level < 20:
        return "Demon"
    elif level == 20:
        return "Demon lord"


def graphics(turn, level):
    name = get_name(level)
    menu = ['│ATTACK│', ' MAGIC ', ' INVENTORY ']
    attack_skills = ['│SKILL 1│', ' SKILL 2 ', ' SKILL 3 ']
    magic_skills = ['│MAGIC 1│', ' MAGIC 2 ', ' MAGIC 3 ']
    inventory = ['│ITEM 1│', ' ITEM 2 ', ' ITEM 3 ']
    choose = 0
    while choose < 1:
        util.clear_screen()
        print('you', '                 ', name)
        print('--------------------------------')
        if turn == 0:
            print('Your turn')
        else:
            print('Enemy turn')
        print('level:', inventory_sys.YOUR_LEVEL['level'], '               level:', level)
        print(YOUR_STAT['health'], 'HP                     ', ENEMY_STAT['health'], 'HP')
        print(YOUR_STAT['mana'], 'MP')
        print('--------------------------------')
        if turn == 0:
            print(" ")
            print(menu[0], "   ", menu[1], "   ", menu[2])
            if menu[0] == '│ATTACK│':
                tabs('ATTACK', attack_skills, magic_skills, inventory)
            elif menu[1] == '│MAGIC│':
                tabs('MAGIC', attack_skills, magic_skills, inventory)
            else:
                tabs('INVENTORY', attack_skills, magic_skills, inventory)
            choose = menu_nav(menu, attack_skills, magic_skills, inventory, )
        else:
            feed = enemy_ai(name)
            print(" ")
            print(*feed)
            time.sleep(2)
            choose = 1


def tabs(tab, attack_skills, magic_skills, inventory):
    attack = skills.return_skills("attack")
    magic = skills.return_skills("magic")
    eqp_inventory = skills.return_skills("inventory")
    i = 0
    if tab == 'ATTACK':
        for index in attack_skills:
            print(attack_skills[i], attack[i])
            i += 1
    elif tab == 'MAGIC':
        for index in magic_skills:
            print(magic_skills[i], magic[i])
            i += 1
    else:
        for index in inventory:
            print(inventory[i], eqp_inventory[i])
            i += 1


def menu_nav(menu, attack_skills, magic_skills, inventory, ):
    original_menu = [' ATTACK ', ' MAGIC ', ' INVENTORY ']
    menu_mark = ['│ATTACK│', '│MAGIC│', '│INVENTORY│']
    original_attack_skills = [' SKILL 1 ', ' SKILL 2 ', ' SKILL 3 ']
    original_magic_skills = [' MAGIC 1 ', ' MAGIC 2 ', ' MAGIC 3 ']
    original_inventory = [' ITEM 1 ', ' ITEM 2 ', ' ITEM 3 ']
    mark_attack_skills = ['│SKILL 1│', '│SKILL 2│', '│SKILL 3│']
    mark_magic_skills = ['│MAGIC 1│', '│MAGIC 2│', '│MAGIC 3│']
    mark_inventory = ['│ITEM 1│', '│ITEM 2│', '│ITEM 3│']
    menu_input = util.key_pressed()
    if menu_input == "d":
        if menu[0] == menu_mark[0]:
            menu[0] = original_menu[0]
            menu[1] = menu_mark[1]
        elif menu[1] == menu_mark[1]:
            menu[1] = original_menu[1]
            menu[2] = menu_mark[2]
        return 0
    elif menu_input == "a":
        if menu[1] == menu_mark[1]:
            menu[1] = original_menu[1]
            menu[0] = menu_mark[0]
        elif menu[2] == menu_mark[2]:
            menu[2] = original_menu[2]
            menu[1] = menu_mark[1]
        return 0
    elif menu_input == "s":
        if menu[0] == menu_mark[0]:
            if attack_skills[0] == mark_attack_skills[0]:
                attack_skills[0] = original_attack_skills[0]
                attack_skills[1] = mark_attack_skills[1]
            elif attack_skills[1] == mark_attack_skills[1]:
                attack_skills[1] = original_attack_skills[1]
                attack_skills[2] = mark_attack_skills[2]
        elif menu[1] == menu_mark[1]:
            if magic_skills[0] == mark_magic_skills[0]:
                magic_skills[0] = original_magic_skills[0]
                magic_skills[1] = mark_magic_skills[1]
            elif magic_skills[1] == mark_magic_skills[1]:
                magic_skills[1] = original_magic_skills[1]
                magic_skills[2] = mark_magic_skills[2]
        elif menu[2] == menu_mark[2]:
            if inventory[0] == mark_inventory[0]:
                inventory[0] = original_inventory[0]
                inventory[1] = mark_inventory[1]
            elif inventory[1] == mark_inventory[1]:
                inventory[1] = original_inventory[1]
                inventory[2] = mark_inventory[2]
        return 0
    elif menu_input == "w":
        if menu[0] == menu_mark[0]:
            if attack_skills[2] == mark_attack_skills[2]:
                attack_skills[2] = original_attack_skills[2]
                attack_skills[1] = mark_attack_skills[1]
            elif attack_skills[1] == mark_attack_skills[1]:
                attack_skills[1] = original_attack_skills[1]
                attack_skills[0] = mark_attack_skills[0]
        elif menu[1] == menu_mark[1]:
            if magic_skills[2] == mark_magic_skills[2]:
                magic_skills[2] = original_magic_skills[2]
                magic_skills[1] = mark_magic_skills[1]
            elif magic_skills[1] == mark_magic_skills[1]:
                magic_skills[1] = original_magic_skills[1]
                magic_skills[0] = mark_magic_skills[0]
        if menu[2] == menu_mark[2]:
            if inventory[2] == mark_inventory[2]:
                inventory[2] = original_inventory[2]
                inventory[1] = mark_inventory[1]
            elif inventory[1] == mark_inventory[1]:
                inventory[1] = original_inventory[1]
                inventory[0] = mark_inventory[0]
        return 0
    elif menu_input == "e":
        tab = [" "]
        skill_tab = 0
        for row in menu:
            for col in row:
                if col == "│":
                    skill_tab = row
        if skill_tab == "│ATTACK│":
            tab == attack_skills
            skill = get_x(attack_skills)
        elif skill_tab == "│MAGIC│":
            tab == magic_skills
            skill = get_x(magic_skills)
        elif skill_tab == "│INVENTORY│":
            tab == inventory
            skill = get_x(inventory)
        attack(skill_tab, skill)
        return 1
    else:
        return 0


def get_x(menu):
    x = 0
    for row in menu:
        for col in row:
            if col == "│":
                return x
        x += 1


def attack(skill_tab, skill, ):
    if skill_tab == "│ATTACK│":
        skills.return_hit(skill, "attack")
        if YOUR_STAT['mana'] > skills.YOUR_STAT['mana']:
            YOUR_STAT['mana'] = skills.YOUR_STAT['mana']
        else:
            pass
    elif skill_tab == "│MAGIC│":
        skills.return_hit(skill, "magic")
        if YOUR_STAT['mana'] > skills.YOUR_STAT['mana']:
            YOUR_STAT['mana'] = skills.YOUR_STAT['mana']
        else:
            pass
    elif skill_tab == "│INVENTORY│":
        if skill == 0:
            result(10, 0, 0, "inv")
        elif skill == 1:
            result(0, 10, 0, "inv")
        else:
            result(0, 20, 0, "inv")


def result(hp_hit, mana_consumption, enemy_hit, hit_type):
    YOUR_STAT['health'] += hp_hit
    YOUR_STAT['mana'] += mana_consumption
    ENEMY_STAT['health'] -= enemy_hit
    if YOUR_STAT['health'] > skills.YOUR_STAT['health']:
        YOUR_STAT['health'] = skills.YOUR_STAT['health']
    if YOUR_STAT['mana'] > skills.YOUR_STAT['mana']:
        YOUR_STAT['mana'] = skills.YOUR_STAT['mana']


def enemy_ai(name):
    rand = random.randint(0, 10)
    if rand > 8:
        ENEMY_STAT['health'] += ENEMY_STAT['attack']
        enemy_feed = (name, "healed itself with ", ENEMY_STAT['attack'], " hp point")
        if ENEMY_STAT['health'] > ENEMY_STAT['og_health']:
            ENEMY_STAT['health'] = ENEMY_STAT['og_health']
        return enemy_feed
    else:
        YOUR_STAT['health'] -= ENEMY_STAT['attack']
        enemy_feed = (name, "hit you with ", ENEMY_STAT['attack'], " damage")
        return enemy_feed


def fight(level):
    turn = 0
    lose = 0
    while lose < 1:
        if ENEMY_STAT['health'] < 1:
            lose = 2
        elif YOUR_STAT['health'] < 1:
            lose = 3
        elif turn == 1:
            graphics(turn, level)
            turn = 0
        elif turn == 0:
            graphics(turn, level)
            turn = 1
    return lose
