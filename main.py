from random import randint
from time import sleep
import os

# Utility to clear the console
clear = lambda: os.system('clear')

hero = {
    'name': '',
    'hp': 100,
    'xp': 0,
    'backpack': {
        'superpotions': 0,
        'has_spellbook': False,
        'has_fireball': False
    }
}
day = 1

def reset():
    global hero, day
    hero.update({
        'name': '',
        'hp': 100,
        'xp': 0,
        'backpack': {
            'superpotions': 0,
            'has_spellbook': False,
            'has_fireball': False
        }
    })
    day = 1

def showStat():
    clear()
    print(f'📅 Day {day}')
    print(f'💖 HP: {hero["hp"]} | 🌟 XP: {hero["xp"]}')
    print('🧺 Backpack:')
    print(f'  💪 Superpotions: {hero["backpack"]["superpotions"]}')
    print(f'  📖 Spellbook: {"Found" if hero["backpack"]["has_spellbook"] else "Not Found"}')
    print(f'  🔥 Fireball Spell: {"Learned" if hero["backpack"]["has_fireball"] else "Not Learned"}')

def gameOver():
    showStat()
    print('\n💀 GAME OVER 💀')
    print(f'{hero["name"]} has perished in the cursed forest.')
    input('Press ENTER to play again.')
    reset()
    startGame()

def endGame():
    showStat()
    print('\n🎉 CONGRATULATIONS 🎉')
    print(f'{hero["name"]} survived 10 days and gained {hero["xp"]} XP!')
    input('Press ENTER to play again.')
    reset()
    startGame()

def noFight():
    print('Hero decided to avoid the fight... ⚔️')
    sleep(1)
    if randint(0, 100) < 60:  # 60% chance to find a potion
        print('You found a potion!')
        drink = input('Do you want to drink it? [Y/n] ').lower()
        if drink == '' or 'y' in drink:
            potion_effect = randint(-20, 20)
            hero['hp'] += potion_effect
            if potion_effect > 0:
                print(f'😊 The potion healed you for {potion_effect} HP!')
            else:
                print(f'🤨 The potion was poisonous! You lost {-potion_effect} HP.')
            if hero['hp'] <= 0:
                gameOver()
        else:
            print('You decided not to drink the potion.')
    else:
        print('You didn\'t find anything useful.')
    sleep(1)

def fight():
    print('Hero decided to fight a goblin... ⚔️')
    sleep(1)
    if hero['backpack']['has_fireball']:
        print('🔥 Hero used Fireball! The goblin was incinerated instantly!')
        damage = 0
    else:
        damage = randint(10, 30)
        print(f'The goblin attacked! You took {damage} damage.')

    xp_gain = randint(10, 25)
    hero['hp'] -= damage
    hero['xp'] += xp_gain
    print(f'🌟 You gained {xp_gain} XP!')
    if hero['hp'] <= 0:
        gameOver()
    elif hero['backpack']['has_spellbook'] and randint(0, 100) < 15:  # 15% chance for superpotion
        hero['backpack']['superpotions'] += 1
        print('💪 You found a superpotion and stored it in your backpack!')
    sleep(1)

# Morning phase
def morning():
    showStat()
    print('🌅 Morning arrives...')
    if hero['backpack']['superpotions'] > 0:
        use_superpotion = input('Do you want to drink a superpotion? [Y/n] ').lower()
        if use_superpotion == '' or 'y' in use_superpotion:
            hero['hp'] = 100
            hero['backpack']['superpotions'] -= 1
            print('💪 You drank a superpotion and restored your HP to 100!')
    sleep(1)

# Evening phase
def evening():
    if day == 5:
        hero['backpack']['has_spellbook'] = True
        print('📖 You found a mysterious spellbook!')
    if hero['backpack']['has_spellbook'] and hero['xp'] > 100 and not hero['backpack']['has_fireball']:
        hero['backpack']['has_fireball'] = True
        print('🔥 You learned the Fireball spell from the spellbook!')
    sleep(1)

def startGame():
    global day, hero
    reset()
    clear()

    hero['name'] = input('Enter your hero\'s name: ')
    print(f'Welcome, {hero["name"]}! Your goal is to survive 10 days in the cursed forest.')
    input('Press ENTER to begin your journey.')
    clear()

    while day <= 10:
        morning()

        want_to_fight = input('Fight a goblin? [Y/n] ').lower()
        if want_to_fight == '' or 'y' in want_to_fight:
            fight()
        else:
            noFight()

        evening()

        input('Press ENTER to continue...')
        clear()
        if hero['hp'] > 0:
            day += 1

    endGame()

startGame()
