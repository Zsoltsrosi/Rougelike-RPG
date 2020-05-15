import util


def help():
    util.clear_screen()
    print("Your main objective is to get to the 21st dungeon to escape","You can move with W A S D keys.")
    print("If you feel like you are not strong enough you can switch weapons and, skills via the inventory key (I)")
    print("In the inventory you have to navigate with the default controls.")
    print("If you see what weapon you want to use navigate to it and press e to equip. (You can only use 1 weapon and or, armor at once and, 3 of booth skill types)")
    print("You can loot and level up by killing enemys, the more you go on the harder the enemy will be but the reward will be plenty.")
    print("You only have one life if you die you have to start it again. Unlike in reality you can retry whenever you want.")
    util.key_pressed()


def logo(logo_type):
    if logo_type == "win":
        print('''
          _______                      _______  _       
|\     /|(  ___  )|\     /|  |\     /|(  ___  )( (    /|
( \   / )| (   ) || )   ( |  | )   ( || (   ) ||  \  ( |
 \ (_) / | |   | || |   | |  | | _ | || |   | ||   \ | |
  \   /  | |   | || |   | |  | |( )| || |   | || (\ \) |
   ) (   | |   | || |   | |  | || || || |   | || | \   |
   | |   | (___) || (___) |  | () () || (___) || )  \  |
   \_/   (_______)(_______)  (_______)(_______)|/    )_)
                                                        ''')
    elif logo_type == "lose":
        print('''
          _______             _        _______  _______ _________
|\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \\__   __/
( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/   ) (   
 \ (_) / | |   | || |   | |  | |      | |   | || (_____    | |   
  \   /  | |   | || |   | |  | |      | |   | |(_____  )   | |   
   ) (   | |   | || |   | |  | |      | |   | |      ) |   | |   
   | |   | (___) || (___) |  | (____/\| (___) |/\____) |   | |   
   \_/   (_______)(_______)  (_______/(_______)\_______)   )_(                                                                            
        ''')
