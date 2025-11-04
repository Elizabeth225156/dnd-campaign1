import random as random

class_skill_options = {
    "barbarian": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
    "bard": ["Any"],
    "cleric": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
    "druid": ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
    "fighter": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    "monk": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
    "paladin": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
    "ranger": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
    "rogue": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
    "sorcerer": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
    "warlock": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
    "wizard": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
}

class Character_Sheet:
    def __init__(self):
        self.name = ""
        self.class_ = ""
        self.level = 0
        self.experience_points = ""
        self.race = ""
        self.background = ""
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.skills_ = []
        self.weapons = []
        self.spells = []
        self.cantrips = []
        self.initiative = 0
        self.speed = 0
        self.hit_points = 0
        self.feats = []
        self.features = []
        self.inventory = []


    def to_dict(self):
        return {
            "name": self.name,
            "class_": self.class_,
            "level": self.level,
            "experience_points": self.experience_points,
            "race": self.race,
            "background": self.background,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "skills": self.skills_,
            "speed": self.speed,
            "inventory": self.inventory,
            "armor": {
                "type": self.armor_type,
                "shield": self.shield,
            }
        }

    def __str__(self):
        return "Name: " + self.name + "\nClass: " +  self.class_ + "\nRace: " + self.race + "\nBackground: " + self.background
    
    def base_stats(self, name: str, class_: str, race: str, background: str):        
        self.name = name
        self.class_ = class_
        self.race = race
        self.background = background

    def ability_score(self):
        values = [15, 14, 13, 12, 10, 8]
        random.shuffle(values)

        self.strength = values[0]
        self.dexterity = values[1]
        self.constitution = values[2]
        self.intelligence = values[3]
        self.wisdom = values[4]
        self.charisma = values[5]
    
    def prof_bonus(self, prof_bonus: str):
        self.prof_bonus = prof_bonus
        match prof_bonus:
            case 'strength':
                self.strength += 2
                print("\tNew strength: " + str(self.strength))
            case 'dexterity':
                self.dexterity += 2
                print("\tNew dexterity: " + str(self.dexterity))
            case 'constitution':
                self.constitution += 2
                print("\tNew constitution: " + str(self.constitution))
            case 'intelligence':
                self.intelligence += 2
                print("\tNew intelligence: " + str(self.intelligence))
            case 'wisdom':
                self.wisdom += 2
                print("\tNew wisdom: " + str(self.wisdom))
            case 'charisma':
                self.charisma += 2
                print("\tNew charimsa: " + str(self.charisma))
            case _:
                print("\tsilly silly doesn't want one...")

    def skills(self):
        class_name = self.class_.lower()
        num_of_skills = {
            "barbarian": 2, "bard": 3, "cleric": 2, "druid": 2, "fighter": 2,
            "monk": 2, "paladin": 2, "ranger": 3, "rogue": 4, "sorcerer": 2,
            "warlock": 2, "wizard": 2
        }.get(class_name, 0)

        options = class_skill_options.get(class_name, [])
        selected_skills = []

        print(f"\nChoose {num_of_skills} skills from the following:")
        if options == ["Any"]:
            # Let bard choose from all skills
            options = ["acrobatics", "animal handling", "arcana", "athletics", "deception", "history",
                    "insight", "intimidation", "investigation", "medicine", "nature", "perception",
                    "performance", "persuasion", "religion", "sleight of hand", "stealth", "survival"]

        for skill in options:
            print(f" - {skill}")

        while len(selected_skills) < num_of_skills:
            choice = input("Enter a skill: ").strip()
            if choice in options and choice not in selected_skills:
                selected_skills.append(choice)
            else:
                print("Invalid or duplicate skill.")

        self.skills = selected_skills
        print(f"\nSelected skills: {', '.join(self.skills)}")

    def armor(self, armor_type, armor_class, shield, armor_prof):
        self.armor_type = armor_type
        self.armor_class = armor_class
        self.shield = shield
        self.armor_prof = armor_prof
        self.initiative = 0
        self.speed = 0
        self.hit_points = 0
