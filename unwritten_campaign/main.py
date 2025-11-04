import random
import classes.weapons as weapons
import classes.magic as magic
import classes.character as character
import classes.ai as ai

ai = ai.AI()
char_sheet = character.Character_Sheet()

def check_input(user_input: str, options: list[str]) -> bool:
    return user_input in options

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
    base_stats.append(input(text[i]))
    match i:
        case 1:
            #class
            while(check_input(base_stats[i], classes) == False):
                base_stats[1] = input(text[i])
        case 2:
            #race
            while(check_input(base_stats[i], races) == False):
                base_stats[2] = input(text[i])
        case 3:
            #background
            while(check_input(base_stats[i], backgrounds) == False):
                base_stats[3] = input(text[i])
        
char_sheet.base_stats(base_stats[0], base_stats[1], base_stats[2], base_stats[3])

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

armor_type = input("Enter armor type (light, medium, heavy): ")
shield = input("Do you use a shield? (yes/no): ")

if is_valid_armor_input(char_sheet.class_, armor_type, shield):
    print("Armor input accepted.")
    char_sheet.armor_type = armor_type
    char_sheet.shield = shield
else:
    print("Invalid armor or shield choice for your class.")


#Weapon and magic selection. It isn't working yet.
# weapon_profs = weapons.get_total_weapon_proficiencies(char_sheet.class_, char_sheet.race, char_sheet.background)

# available_weapons = weapons.filter_weapons_by_proficiency(weapon_profs)
# print("Available weapons:", available_weapons)

# available_weapons = weapons.filter_weapons_by_proficiency(weapon_profs)

# for i in available_weapons:
#     # print(available_weapons)
#     print(f" - {i}")
# weapon_choice = input("\tChoose your weapon: ")
# char_sheet.weapons.append(weapon_choice)

# spell_types = magic.get_total_spells(char_sheet.class_)
# available_spells = magic.filter_spells_by_access(spell_types)

# for s in available_spells:
#     print(f" - {s}")
# spell_choice = input("\tChoose your spell: ")
# char_sheet.spells.append(spell_choice)

#Generate backstory
prompt = "Generate the beginning of a dnd campaign with the character previously defined"
player_character = char_sheet.to_dict()
ai.generate_backstory(player_character)
ai.start_quest(prompt)
#Start quest
for i in range(0, 10):
    prompt = input("\n\tWhat would you like to do next: ")
    ai.next_chapter(prompt)
ai.ending_prompt(prompt)
