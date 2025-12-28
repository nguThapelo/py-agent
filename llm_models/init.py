#llm_model/__init__.py
from .gpt3 import GPT3
from .gpt4 import GPT4
from .rag import RAG

# Get model def
def get_llm_model(model_name):
    if model_name == "gpt3":
        return GPT3()
    elif model_name == "gpt4":
        return GPT4()
    elif model_name == "rag":
        return RAG()
    else:
        raise ValueError("Invalid model name")
