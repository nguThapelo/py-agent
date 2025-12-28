#llm_models/gpt4.py
import openai

#define gpt4 model
class GPT4: 
    def __init__(self):
        self.api_key = "api"
        self.model_name = "prompt me later"

    def generate_text(self, prompt):
        #generate text from openai 
        response = openai.Completion.create(
            engine = self.model_name,
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.5
        )
        return response.choices[0].text.strip()