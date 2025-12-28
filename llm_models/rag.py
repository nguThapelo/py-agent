# llm_models/rag.py

from transformers import RagTokenizer, RagModel
import torch

class RAG:
    def __init__(self):
        self.tokenizer = RagTokenizer.from_pretrained("facebook/rag-tokenizer")
        self.model = RagModel.from_pretrained("facebook/rag-model")

    def generate_text(self, prompt):
        # Use RAG model 
        inputs = self.tokenizer(prompt, return_tensonrs="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens = True)