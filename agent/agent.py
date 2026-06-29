from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from config import GOOGLE_API_KEY
from agent.prompt import SYSTEM_PROMPT
from agent.memory import memory

from tools.order_tool import get_order
from tools.product_tool import get_product
from tools.search_tool import search_products
from tools.recommendation_tool import (
    find_cheaper_products,
    best_rated_products,
)
from tools.inventory_tool import check_stock
from tools.tracking_tool import track_order

tools = [
    get_order,
    get_product,
    search_products,
    find_cheaper_products,
    best_rated_products,
    check_stock,
    track_order,
]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0,
)

agent = create_react_agent(
    model=model,
    tools=tools,
    prompt=SYSTEM_PROMPT
)