from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import Tool
from datetime import datetime


def save_to_txt(data: str, filename: str = None) -> str:
    """Saves the given data to a text file with a timestamped filename.

    Args:
        data (str): The data to be saved to the text file.
        filename (str, optional): The base name for the file. If not provided,
                                  a default name with timestamp will be used.

    Returns:
        str: The path to the saved text file.
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)
    
    return f"Data saved to {filename}"

save_tool = Tool(
    name="save_to_txt",
    func=save_to_txt,
    description="Saves the provided text data to a timestamped text file. Input should be a string of text to save."
)

search = DuckDuckGoSearchRun
search_tool = Tool(
    name="search_online",
    func=search.run,
    description="Useful for when you need to answer questions about current events or find specific information online.",
)


# api_wrapper = WikipediaAPIWrapper(
#     top_k_results=1, 
#     doc_content_chars_max=100,
#     load_max_docs=1000
# )

# wikipedia_tool = Tool(
#     name="wikipedia_lookup",
#     func=api_wrapper.run,
#     description="Useful for when you need to look up information about people, places, or thingson Wikipedia.",

# )

# wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)


