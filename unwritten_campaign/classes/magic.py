class_spell_lists = {
    "Wizard": ["Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy", "Transmutation"],
    "Cleric": ["Abjuration", "Divination", "Evocation", "Necromancy", "Transmutation", "Healing", "Protection", "Divine"],
    "Druid": ["Conjuration", "Divination", "Evocation", "Transmutation", "Nature", "Beast", "Elemental"],
    "Sorcerer": ["Evocation", "Enchantment", "Transmutation", "Illusion", "Divination", "Necromancy"],
    "Warlock": ["Evocation", "Enchantment", "Necromancy", "Divination", "Conjuration", "Dark"],
    "Bard": ["Enchantment", "Illusion", "Transmutation", "Divination", "Charm", "Support"],
    "Paladin": ["Abjuration", "Evocation", "Divination", "Healing", "Protection"],
    "Ranger": ["Conjuration", "Divination", "Evocation", "Transmutation", "Nature", "Beast"],
    "Artificer": ["Transmutation", "Abjuration", "Evocation", "Support", "Craft"],
}

def get_total_spells(char_class):
    char_class = char_class.title()  # Ensures "wizard" becomes "Wizard"
    spells = set()
    spells.update(class_spell_lists.get(char_class, []))
    return list(spells)

def filter_spells_by_access(spell_types):
    all_spells = {
        "Magic Missile": "Evocation",
        "Shield": "Abjuration",
        "Cure Wounds": "Healing",
        "Entangle": "Nature"
    }
    return [s for s, school in all_spells.items() if school in spell_types]

class Magic:
    def __init__(self, name, school_of_magic, casting_time, range, duration, components, material_requirements, damage_type, saving_throw, spell_save_dc, spell_attack_bonus, concentration, ritual, casting_class, required_level, cooldown):
        self.name = name
        self.school_of_magic = school_of_magic
        self.casting_time = casting_time
        self.range = range
        self.duration = duration
        self.components = components
        self.material_requirements = material_requirements
        self.damage_type = damage_type
        self.saving_throw = saving_throw
        self.spell_save_dc = spell_save_dc
        self.spell_attack_bonus = spell_attack_bonus
        self.concentration = concentration
        self.ritual = ritual
        self.casting_class = casting_class
        self.required_level = required_level
        self.cooldown = cooldown