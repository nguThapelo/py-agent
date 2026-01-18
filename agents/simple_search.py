from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
# from langchain import initialize_agent, AgentExecutor
from tools.tools import search_tool #, save_to_txt, wiki_tool

load_dotenv()  # Load environment variables

# Define the structured output model
class ResponseModel(BaseModel):
    message: str
    summary: str
    source: list[str]
    tools_used: list[str]

# Initialize OpenAI LLM
openai_llm2 = ChatOpenAI(model_name="gpt-4o-mini")

# Parser and prompt
parser = PydanticOutputParser(pydantic_object=ResponseModel)
prompt = ChatPromptTemplate.from_template(
    """Respond to the user message and provide a summary, sources, and tools used in the response.
    {format_instructions}
    {chat_history}
    User Message: {user_message}
    {query}
    {agent_scratchpad}
    """
).partial(format_instructions=parser.get_format_instructions())

# Tools
tools = [search_tool #, save_to_txt, wiki_tool
         ]

# def get_agent_executor() -> AgentExecutor:
#     """Return a ready-to-use AgentExecutor"""
#     agent = initialize_agent(
#         openai_llm2=openai_llm2,
#         prompt=prompt,
#         tools=tools,
#         verbose=True
#     )
#     agent_executor = AgentExecutor.from_agent_and_tools(
#         agent=agent,
#         tools=tools,
#         verbose=True
#     )
#     return agent_executor

def generate_response(user_message: str, chat_history: str = "") -> ResponseModel:
    """Generate a structured response from the agent."""
    response = openai_llm2.generate_prompt(
        [
            prompt.format_prompt(
                format_instructions=parser.get_format_instructions(),
                chat_history=chat_history,
                user_message=user_message,
                query="Additional query context goes here.",
                agent_scratchpad="Agent's scratchpad content goes here."
            )
        ]
    )
    output = parser.parse(response.generations[0][0].text)
    return output
