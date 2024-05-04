wizard = "Wizard"
elf = "Elf"
human = "Human"

wand = "Wand"
bow = "Bow"
sword = "Sword"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_dmg = 150
elf_dmg = 100
human_dmg = 75

match__dmg = 1.5
mismatch_dmg = .8
nomatch_dmg = 1.1

dragon_hp = 300
dragon_dmg = 50

dmg_bonus = 1

round = 0

while True:
    print("1) Wizard\n2) Elf\n3) Human")
    character = input("Choose your character: ")

    print("1) Sword\n2) Wand\n3) Bow")
    weapon = input("Choose your weapon: ")

    if character == "1" or character == "Wizard":
        character = "Wizard"
        my_hp = wizard_hp
        my_dmg = wizard_dmg
        if weapon == "2" or weapon == "Wand":
            dmg_bonus = match__dmg
            weapon = "Wand"
        elif weapon == "1" or weapon == "Sword":
            dmg_bonus == mismatch_dmg
            weapon = "Sword"
        elif weapon == "3" or weapon == "Bow":
            dmg_bonus == nomatch_dmg
            weapon = "Bow"
        else:
            weapon = "Unknown Weapon"
        break
    elif character == "2" or character == "Elf":
        character = "Elf"
        my_hp = elf_hp
        my_dmg = elf_dmg
        if weapon == "3" or weapon == "Bow":
            dmg_bonus = match__dmg
            weapon = "Bow"
        elif weapon == "1" or weapon == "Sword":
            dmg_bonus == mismatch_dmg
            weapon = "Sword"
        elif weapon == "2" or weapon == "Wand":
            dmg_bonus == nomatch_dmg
            weapon = "Wand"
        else:
            weapon = "Unknown Weapon"
        break
    elif character == "3" or character == "Human":
        character = "Human"
        my_hp = human_hp
        my_dmg = human_dmg
        if weapon == "1" or weapon == "Sword":
            dmg_bonus = match__dmg
            weapon = "Sword"
        elif weapon == "2" or weapon == "Wand":
            dmg_bonus == mismatch_dmg
            weapon = "Wand"
        elif weapon == "3" or weapon == "Bow":
            dmg_bonus == nomatch_dmg
            weapon = "Bow"
        else:
            weapon = "Unknown Weapon"
        break
    else:
        print("Unknown Character")

#Display Character Details

print(f"\nUser selected {character} & {weapon}...\nHealth = {my_hp}\nDamage = {my_dmg}\nDamage Bonus = {dmg_bonus}\n")

#Battle 

if dmg_bonus == 1.5:
    print(f"::: Max Damage!! :::\n")
print(f"The Dragon has challenged the {character}\nDragon Health = {dragon_hp}\nDragon Damage = {dragon_dmg}\n")
my_dmg = my_dmg*dmg_bonus

while True:
        round += 1
        dragon_hp = dragon_hp - my_dmg
        print(f"\nRound {round}")
        print(f"\nThe {character} has damaged the dragon for {my_dmg}!\nDragon Health = {dragon_hp}")
        if dragon_hp <= 0:
            print(f"The Dragon has been defeated in {round} Rounds!\nThe {character} has {my_hp} Health remaining!\n")
            break

        my_hp = my_hp - dragon_dmg
        print(f"\n\nThe Dragon has damaged the {character} for {dragon_dmg}!\n{character} Health = {my_hp}")
        if my_hp <= 0:
            print(f"The {character} has been defeated...\n")
            break


"""
Notes:

Bonus Damage Idea:
Allow user to select a weapon, if weapon is a "match" to their character-style they get bonus dmg:

match = dmg * 1.5
mismatch = dmg *.8
nomatch = dmg * 1.1

Weapon matching logic/rules:

wizard wpn - match wand, mismatch sword, nomatch bow
elf wpn - match bow, mismatch sword, nomatch wand
human wpn - match sword, mismatch wand, nomatch bow
"""