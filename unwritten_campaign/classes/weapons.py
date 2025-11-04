class_weapon_profs = {
    "Fighter": ["Simple", "Martial"],
    "Wizard": ["Simple"],
    "Rogue": ["Simple", "Hand Crossbow", "Rapier", "Shortsword"]
}

background_weapon_profs = {
    "Soldier": ["Martial", "Shield"],
    "Noble": ["Rapier"],
    "Criminal": ["Dagger", "Shortsword"]
}

race_weapon_profs = {
    "Elf": ["Longbow", "Shortsword"],
    "Dwarf": ["Battleaxe", "Warhammer"]
}

def get_total_weapon_proficiencies(char_class, race, background):
    char_class = char_class.title()
    race = race.title()
    background = background.title()

    profs = set()
    profs.update(class_weapon_profs.get(char_class, []))
    profs.update(background_weapon_profs.get(background, []))
    profs.update(race_weapon_profs.get(race, []))


    profs = set()
    profs.update(class_weapon_profs.get(char_class, []))
    profs.update(background_weapon_profs.get(background, []))
    profs.update(race_weapon_profs.get(race, []))
    return list(profs)

def filter_weapons_by_proficiency(proficiencies):
    proficiencies = [i.lower() for i in proficiencies]
    all_weapons = [
    {
        "name": "Dagger",
        "type": "melee",
        "proficiency": "simple",
        "damage": "1d4",
        "damage_type": "piercing",
        "properties": ["finesse", "light", "thrown"]
    },
    {
        "name": "Shortsword",
        "type": "melee",
        "proficiency": "martial",
        "damage": "1d6",
        "damage_type": "piercing",
        "properties": ["finesse", "light"]
    },
    {
        "name": "Longsword",
        "type": "melee",
        "proficiency": "martial",
        "damage": "1d8",
        "damage_type": "slashing",
        "properties": ["versatile"]
    },
    {
        "name": "Greatsword",
        "type": "melee",
        "proficiency": "martial",
        "damage": "2d6",
        "damage_type": "slashing",
        "properties": ["heavy", "two-handed"]
    },
    {
        "name": "Rapier",
        "type": "melee",
        "proficiency": "martial",
        "damage": "1d8",
        "damage_type": "piercing",
        "properties": ["finesse"]
    },
    {
        "name": "Quarterstaff",
        "type": "melee",
        "proficiency": "simple",
        "damage": "1d6",
        "damage_type": "bludgeoning",
        "properties": ["versatile"]
    },
    {
        "name": "Handaxe",
        "type": "melee",
        "proficiency": "simple",
        "damage": "1d6",
        "damage_type": "slashing",
        "properties": ["light", "thrown"]
    },
    {
        "name": "Battleaxe",
        "type": "melee",
        "proficiency": "martial",
        "damage": "1d8",
        "damage_type": "slashing",
        "properties": ["versatile"]
    },
    {
        "name": "Shortbow",
        "type": "ranged",
        "proficiency": "simple",
        "damage": "1d6",
        "damage_type": "piercing",
        "properties": ["two-handed"]
    },
    {
        "name": "Longbow",
        "type": "ranged",
        "proficiency": "martial",
        "damage": "1d8",
        "damage_type": "piercing",
        "properties": ["heavy", "two-handed"]
    },
    {
        "name": "Crossbow, Light",
        "type": "ranged",
        "proficiency": "simple",
        "damage": "1d8",
        "damage_type": "piercing",
        "properties": ["loading", "two-handed"]
    },
    {
        "name": "Crossbow, Heavy",
        "type": "ranged",
        "proficiency": "martial",
        "damage": "1d10",
        "damage_type": "piercing",
        "properties": ["heavy", "loading", "two-handed"]
    },
    {
        "name": "Mace",
        "type": "melee",
        "proficiency": "simple",
        "damage": "1d6",
        "damage_type": "bludgeoning",
        "properties": []
    },
    {
        "name": "Warhammer",
        "type": "melee",
        "proficiency": "martial",
        "damage": "1d8",
        "damage_type": "bludgeoning",
        "properties": ["versatile"]
    }
    ]

    return [
        w["name"]
        for w in all_weapons
        if w["proficiency"].lower() in proficiencies or w["name"].lower() in proficiencies
    ]



class Weapon:
    def __init__(self, name, type, damage_die, damage_type, properties, range, weight, profficiencies_needed, attack_bonus, magical, ammo_type, special_effects):
        self.name = name
        self.type = type
        self.damage_die = damage_die
        self.damage_type = damage_type
        self.properties = properties
        self.range = range
        self.weight = weight
        self.profficiencies_needed = profficiencies_needed
        self.attack_bonus = attack_bonus
        self.magical = magical
        self.ammo_type = ammo_type
        self.special_effects = special_effects
