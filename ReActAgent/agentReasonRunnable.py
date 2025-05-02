from langchain.agents import tool, create_react_agent
import datetime
from langchain_community.tools import TavilySearchResults
from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

@tool
def my_IceCream_Flavour(format: str = "Name"):
    """ Returns the best flavour of my icecream"""

    return "Vanilla"

@tool
def CalculationTools(expression: str):
    """Evaluates a simple math expression like 'addition, subtraction, Multiply or divide' and returns the result"""

    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error evaluating expression: {e}"

tools = [
    get_system_time,
    my_IceCream_Flavour,
    CalculationTools,
    search_tool,
]

react_prompt = hub.pull("hwchase17/react")

react_agent_runnable = create_react_agent( tools=tools, llm=llm, prompt=react_prompt )