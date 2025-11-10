import random
import classes.weapons as weapons
import classes.magic as magic
import classes.character as character
import classes.ai as ai
import textwrap

def wrapped_print(text, width=70):
    print(textwrap.fill(text, width=width))

char_sheet = character.Character_Sheet()

def check_input(user_input: str, options: list[str]) -> bool:
    return user_input.lower() in [opt.lower() for opt in options]

def roll_dice(num_sides, num_dice, modifier):
    return sum(random.randint(1, num_sides) for _ in range(num_dice)) + modifier

base_stats = []
ability_scores = []
armor_info = []
text = ["\tCharacter name: ", "\tClass: ", "\tRace: ", "\tBackground: ",
        "\tArmor type: ", "\tShield: "]

classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
races = ["human", "elf", "dwarf", "halfling", "gnome", "half-orc", "half-elf", "dragonborn", "tiefling"]
backgrounds = ["acolyte", "charlatan", "criminal", "entertainer", "folk hero", "guild artisan", "hermit", "noble", "outlander", "sage", "sailor", "soldier", "urchin"]

print("Welcome to Unwritten Campaign, an AI generated D&D campaign maker.")
print("Time to create your character")

for i in range(0, 4):
    user_input = input(text[i]).strip()
    base_stats.append(user_input)

    match i:
        case 1:  # class
            while not check_input(base_stats[1], classes):
                base_stats[1] = input(text[i]).strip()
        case 2:  # race
            while not check_input(base_stats[2], races):
                base_stats[2] = input(text[i]).strip()
        case 3:  # background
            while not check_input(base_stats[3], backgrounds):
                base_stats[3] = input(text[i]).strip()
        
char_sheet.base_stats(
    base_stats[0],
    base_stats[1].lower(),
    base_stats[2].lower(),
    base_stats[3].lower()
)


print("\nAbility Scores")
char_sheet.ability_score()
print("\tStrength: " + str(char_sheet.strength) +
        "\n\tDexterity: " + str(char_sheet.dexterity) +
        "\n\tConstitution: " + str(char_sheet.constitution) +
        "\n\tIntelligence: " + str(char_sheet.intelligence) +
        "\n\tWisdom: " + str(char_sheet.wisdom) +
        "\n\tCharimsa: " + str(char_sheet.charisma))

prof_bonus = input("\tProficiency Bonus: ")
char_sheet.prof_bonus(prof_bonus)

char_sheet.skills()

print("Armor stuff")

armor_proficiencies = {
    "barbarian": ["light", "medium", "shield"],
    "bard": ["light"],
    "cleric": ["light", "medium", "shield"],
    "druid": ["light", "medium", "shield"],
    "fighter": ["light", "medium", "heavy", "shield"],
    "monk": [],
    "paladin": ["light", "medium", "heavy", "shield"],
    "ranger": ["light", "medium", "shield"],
    "rogue": ["light"],
    "sorcerer": [],
    "warlock": ["light"],
    "wizard": []
}

def is_valid_armor_input(class_name, armor_type, shield_choice):
    class_name = class_name.lower()
    profs = armor_proficiencies.get(class_name, [])

    armor_ok = armor_type.lower() in profs
    shield_ok = shield_choice.lower() == "yes" if "shield" in profs else shield_choice.lower() == "no"

    return armor_ok and shield_ok

class_name = char_sheet.class_.lower()
profs = armor_proficiencies.get(class_name, [])

if not profs:
    print(f"\nYour class ({char_sheet.class_}) does not have armor or shield proficiency.")
    char_sheet.armor_type = "none"
    char_sheet.shield = "no"
else:
    while True:
        armor_type = input("Enter armor type (light, medium, heavy): ").lower()
        shield = input("Do you use a shield? (yes/no): ").lower()

        if is_valid_armor_input(char_sheet.class_, armor_type, shield):
            print("Armor input accepted.")
            char_sheet.armor_type = armor_type
            char_sheet.shield = shield
            break
        else:
            print("Invalid armor or shield choice for your class. Please try again.\n")



# Weapon and magic selection.
# Weapon selection
weapon_profs = weapons.get_total_weapon_proficiencies(char_sheet.class_, char_sheet.race, char_sheet.background)
available_weapons = weapons.filter_weapons_by_proficiency(weapon_profs)

print("\nAvailable weapons:")
for i in available_weapons:
    print(f" - {i}")

weapon_choice = ""
while weapon_choice.lower() not in [w.lower() for w in available_weapons]:
    weapon_choice = input("\tChoose your weapon: ").strip()
    if weapon_choice.lower() not in [w.lower() for w in available_weapons]:
        print("Invalid choice. Please select a weapon from the list.")

char_sheet.weapons.append(weapon_choice)

# Spell selection
spell_types = magic.get_total_spells(char_sheet.class_)
available_spells = magic.filter_spells_by_access(spell_types)

if not spell_types or not available_spells:
    print(f"\nYour character class ({char_sheet.class_}) does not have access to magic at level 1.")
else:
    print("\nAvailable spells:")
    for s in available_spells:
        print(f" - {s}")

    spell_choice = ""
    while spell_choice.lower() not in [s.lower() for s in available_spells]:
        spell_choice = input("\tChoose your spell: ").strip()
        if spell_choice.lower() not in [s.lower() for s in available_spells]:
            print("Invalid choice. Please select a spell from the list.")

    char_sheet.spells.append(spell_choice)
print()

#Generate backstory
ai = ai.AI(char_sheet)

wrapped_print(ai.generate_backstory())
wrapped_print(ai.scene_creation())

while True:
    user_input = input("\nWhat do you do? ")
    if user_input.lower() in ["end", "quit", "exit"]:
        wrapped_print(ai.end_story())
        break
    wrapped_print(ai.process_input(user_input))
