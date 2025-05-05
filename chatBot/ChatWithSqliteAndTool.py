from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from langchain.agents import tool
from dotenv import load_dotenv
import sqlite3

load_dotenv()

sqlite_conn = sqlite3.connect("checkpoint.sqlite", check_same_thread=False)
memory = SqliteSaver(sqlite_conn)

class BasicChatBot(TypedDict):
    messages: Annotated[list, add_messages]

search_tool = TavilySearchResults(max_results=2)

@tool
def my_IceCream_Flavour(format: str = "Name"):
    """Returns the best flavour of Ram's icecream"""

    return "Vanilla"


@tool
def BestNepalPackage(format: str = "Name"):
    """Returns the best Top 10 package with keyword from Travoires Databases"""
    
    return "Package"

tools = [search_tool, my_IceCream_Flavour, BestNepalPackage]

llm = ChatGroq(model="llama-3.1-8b-instant")
llm_with_tools = llm.bind_tools(tools=tools)

def chatbot(state: BasicChatBot):
    return {
        "messages": [llm_with_tools.invoke(state["messages"])],
    }

def tools_router(state: BasicChatBot):
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0:
        return "tool_node"
    return END

tool_node = ToolNode(tools=tools)

graph = StateGraph(BasicChatBot)
graph.add_node("chatbot", chatbot)
graph.add_node("tool_node", tool_node)
graph.set_entry_point("chatbot")
graph.add_conditional_edges("chatbot", tools_router)
graph.add_edge("tool_node", "chatbot")

app = graph.compile(checkpointer=memory)

thread_id = input("Enter your thread ID (e.g., 1, 2, 'abc123'): ")
config = {"configurable": {"thread_id": thread_id}}

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "end"]:
        break

    result = app.invoke(
        {
            "messages": [HumanMessage(content=user_input)]
        },
        config=config
    )

    print("AI:", result["messages"][-1].content)
