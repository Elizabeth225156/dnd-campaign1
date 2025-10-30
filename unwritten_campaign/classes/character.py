class Character_Sheet:
    def __init__(self):
        self.name = ""
        self.class_ = ""
        self.level = 0
        self.subclass = ""
        self.experience_points = ""
        self.race = ""
        self.background = ""
        self.alignment = ""
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.skills_ = []

    def to_dict(self):
        return {
            "name": self.name,
            "class_": self.class_,
            "level": self.level,
            "subclass": self.subclass,
            "experience_points": self.experience_points,
            "race": self.race,
            "background": self.background,
            "alignment": self.alignment,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "skills": self.skills_
        }

    def __str__(self):
        return "Name: " + self.name + "\nClass: " +  self.class_ + "\nSubclass: " + self.subclass + "\nRace: " + self.race + "\nBackground: " + self.background + "\nAlignment: " + self.alignment
    
    def base_stats(self, name: str, class_: str, subclass: str, race: str, background: str, alignment: str):        
        self.name = name
        self.class_ = class_
        self.subclass = subclass
        self.race = race
        self.background = background
        self.alignment = alignment

    def ability_score(self):
        values = [15, 14, 13, 12, 10, 8]
        #mix up the array
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
                print("silly silly doesn't want one...")

    def skills(self):
        num_of_skills = 0
        match self.class_:
            case 'barbarian':
                num_of_skills = 2 #has more restrictions
            case 'bard':
                num_of_skills = 3
            case 'cleric':
                num_of_skills = 2 #has more restrictions
            case 'druid':
                num_of_skills = 2 #has more restrictions
            case 'fighter':
                num_of_skills = 2 #has more restrictions
            case 'monk':
                num_of_skills = 2 #has more restrictions
            case 'paladin':
                num_of_skills = 2 #has more restrictions
            case 'ranger':
                num_of_skills = 3 #has more restrictions
            case 'rogue':
                num_of_skills = 4 #has more restrictions
            case 'sorcerer':
                num_of_skills = 2 #has more restrictions
            case 'warlock':
                num_of_skills = 2 #has more restrictions
            case 'wizard':
                num_of_skills = 2 #has more restrictions
            case _:
                print("stupid")

        for i in range(0, num_of_skills):
            print("hehehe", i)

    def armor(self):
        #Need armor type, armor class, shield (y/n), armor proficiencies.
        pass

    def magic(self):
        #Spellcasting ability, spell save dc, spell attack bonus, known spells, prepared spells, spell slots, cantrips, magical items
        pass