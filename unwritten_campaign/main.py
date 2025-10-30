import random
import classes.weapons as weapons
import classes.character as character
import classes.ai as ai

ai = ai.AI()
char_sheet = character.Character_Sheet()

def roll_dice(num_for_die):
    return random.randint(0, num_for_die)

def check_input(input):
    if input == 'character sheet':
        pass

base_stats = []
ability_scores = []
text = ["\tCharacter name: ", "\tClass: ", "\tSubclass: ", "\tRace: ", "\tBackground: ", "\tAlignment: "]

print("Welcome to Unwritten Campaign, an AI generated D&D campaign maker.")
print("Time to create your character")

for i in range(0, 6):
    base_stats.append(input(text[i]))
    #Make sure that they enter the correct stuff
char_sheet.base_stats(base_stats[0], base_stats[1], base_stats[2], base_stats[3], base_stats[4], base_stats[5])

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