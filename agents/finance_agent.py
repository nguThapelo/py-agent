import os
from dotenv import load_dotenv
# install phidata
from phi.agent import Agent
from phi.model.openai import OpenAI
from phi.tools.yfinance import YFinanceTools
from phi.knowledge import KnowledgeBase
from phi.storage import InMemoryStorage  # Use Postgres for prod
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Tax/Audit Knowledge Base (add your IRS PDFs/docs here)
tax_kb = KnowledgeBase(
    sources=["Tax deductions include mortgage interest, student loans, and charitable contributions per IRS Pub 529."],
    llm=OpenAI(model="gpt-4o-mini"),
)

# Custom OCR Tool Mock (extend with Tesseract/PaddleOCR)
def ocr_tax_doc(doc_path: str) -> str:
    """Mock OCR for tax receipts - replace with real OCR."""
    return f"Extracted: Income $50k, Deductions: Home office $5k, Charity $2k from {doc_path}"

finance_agent = Agent(
    model=OpenAI(model="gpt-4o-mini"),
    tools=[YFinanceTools(), ocr_tax_doc, tax_kb.get_tools()],
    storage=InMemoryStorage(),  # Persistent memory for audit trails
    description="Expert Finance, Tax & Audit Agent. Analyze stocks, check deductions, validate compliance.",
    instructions=[
        "Use YFinance for stock data/news. Query tax_kb for IRS rules.",
        "For audits: Cross-check numbers, flag anomalies >10%. Output in tables.",
        "Tax: Calculate effective rates, suggest optimizations. Cite sources.",
        "Format responses as markdown with tables for clarity."
    ],
    show_tool_calls=True,
    markdown=True,
)

def process_finance_query(query: str) -> dict:
    response = finance_agent.run(query, stream=False)
    return {"response": response.content, "sources": [t.name for t in response.tools_used or []]}
