import google.generativeai as genai

genai.configure(api_key="AIzaSyBQ6BV1hcUNuNNlzGtYFN9mP4PR0tu-tHM")
model = genai.GenerativeModel("gemini-2.5-flash")

class AI:
    def __init__(self):
        pass

    def response(self, prompt):
        response = model.generate_content(prompt)
        self.last_response = response.texts
        
        print(self.last_response)
        return self.last_response