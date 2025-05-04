from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from langchain.agents import initialize_agent, tool

load_dotenv()

memory = MemorySaver()
search_tool = TavilySearchResults(max_results=2)

@tool
def my_IceCream_Flavour(format: str = "Name"):
    """ Returns the best flavour of my ice cream """
    return "Vanilla"

tools = [search_tool, my_IceCream_Flavour]

llm = ChatGroq(model="llama-3.1-8b-instant")
llm_with_tools = llm.bind_tools(tools=tools)

# Define the state structure for the chatbot
class BasicChatBot(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: BasicChatBot):
    return {
        "messages": [llm_with_tools.invoke(state["messages"])]
    }

def tools_router(state: BasicChatBot):
    last_message = state["messages"][-1]
    
    if hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0:
        return "tool_node"
    else: 
        return END

# Define the tool node
tool_node = ToolNode(tools=tools)

graph = StateGraph(BasicChatBot)

graph.add_node("chatbot", chatbot)
graph.add_node("tool_node", tool_node)

graph.set_entry_point("chatbot")

graph.add_conditional_edges("chatbot", tools_router)
graph.add_edge("tool_node", "chatbot")

app = graph.compile(checkpointer=memory)

config = {"configurable": {
    "thread_id": 1
}}

# Main chat loop
while True: 
    user_input = input("User: ")
    if user_input in ["exit", "end"]:
        break
    else: 
        result = app.invoke({
            "messages": [HumanMessage(content=user_input)]
        }, config=config)

        # Output the AI response
        print("AI: " + result["messages"][-1].content)
