import cohere

co = cohere.Client("replace with your api key")

class AI:
    def __init__(self, character):
        self.character = character
        self.story_log = []

    def generate_backstory(self):
        character_prompt = f"""
    Create a brief (1 short paragraph) backstory for a level 1 {self.character.race} {self.character.class_} named {self.character.name}, with the background of a {self.character.background}. They wield a {self.character.weapons[0]} and wear {self.character.armor_type} armor. Their spell is {self.character.spells[0] if self.character.spells else 'None'}.
    Ability Scores:
    STR {self.character.strength}, DEX {self.character.dexterity}, CON {self.character.constitution}, INT {self.character.intelligence}, WIS {self.character.wisdom}, CHA {self.character.charisma}.
    """
        
        response = co.chat(
            model='command-a-03-2025',
            message=character_prompt,
            temperature=0.5
        )
        backstory = response.text
        self.story_log.append(backstory)

        return backstory
    
    def scene_creation(self):
        scene_prompt = f"""
Begin a D&D 5e campaign for the character above. Use one short paragraph
"""
        response = co.chat(
            model='command-a-03-2025',
            message=scene_prompt,
            temperature=0.5
        )
        scene = response.text
        self.story_log.append(scene)
        return scene

    def process_input(self, user_input):
            prompt = f"""
    Continue the campaign for {self.character.name}. The character has stats {self.character}. The player says: "{user_input}". If a roll is needed, describe it and give the result. Use D&D 5e rules. One short paragraph.
    """
            response = co.chat(
                model='command-a-03-2025',
                message=prompt,
                temperature=0.5
            )
            result = response.text
            self.story_log.append(result)
            return result
    
    def end_story(self):
        ending_prompt = f"""
Conclude the campaign for {self.character.name}. Current story is {self.story_log} Provide a satisfying ending and epilogue. One short paragraph.
"""
        response = co.chat(
            model='command-a-03-2025',
            message=ending_prompt,
            temperature=0.5
        )
        ending = response.text
        self.story_log.append(ending)
        return ending
