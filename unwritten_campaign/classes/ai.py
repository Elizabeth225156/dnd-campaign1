import google.generativeai as genai

genai.configure(api_key="AIzaSyAes7hQyHkallN5qT2APcmECFt-9nd8iVo")
model = genai.GenerativeModel("gemini-2.5-flash")

class AI:
    def __init__(self):
        pass

    def response(self, prompt):
        response = model.generate_content(prompt)
        self.last_response = response.text
        
        print(self.last_response)
        return self.last_response
    
    def generate_backstory(self, character):
        prompt = f"generate a dnd 5e character backstory with:  + {str(character)}"
        response = model.generate_content(prompt)
        self.last_response = response.text
        print(self.last_response)

    def start_quest(self, prompt):
        response = model.generate_content(prompt)
        self.last_response = response.text
        print(self.last_response)

    def next_chapter(self, prompt):
        response = model.generate_content(prompt)
        self.last_response = response.text
        print(self.last_response)

    def ending_prompt(self, prompt):
        prompt = "Generate the last section of a dnd quest"
        response = model.generate_content(prompt)
        self.last_response = response.text
        print(self.last_response)
