from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import datetime
from langchain_openai import ChatOpenAI
from schema import AnswerQuestion, ReviseAnswer
from langchain_core.output_parsers.openai_tools import PydanticToolsParser, JsonOutputToolsParser
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

pydantic_parser = PydanticToolsParser(tools=[AnswerQuestion])

# parser = JsonOutputToolsParser(return_id=True)

# Actor Agent Prompt 
actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are expert AI Searcher.
                Current time: {time}
                    1. {first_instruction}
                    2. Reflect and critique your answer. Be severe to maximize improvement.
                    3. After the reflection, **list 1-3 search queries separately** for researching improvements. Do not include them inside the reflection.
                    4. The context of Problem statement is:
                    ` RainFall predicition system using Recyclable bottle, IOT and AI.`
            """,
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Answer the user's question above using the required format."),
    ]
).partial(
    time=lambda: datetime.datetime.now().isoformat(),
)

first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction="Provide a detailed ~250 word answer"
)

# llm = ChatOpenAI(model="gpt-4o")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


first_responder_chain = first_responder_prompt_template | llm.bind_tools(tools=[AnswerQuestion], tool_choice='AnswerQuestion') 

validator = PydanticToolsParser(tools=[AnswerQuestion])

revise_instructions = """
Revise the following text by deeply enhancing its quality, factual accuracy, and academic credibility using real-world research papers, whitepapers, and verified data sources:

1. Identify weak, vague, or unsupported statements and replace them with strong, well-cited claims from reliable sources.
2. Add numerical citations in the format [1], [2], etc., immediately after each claim or fact.
3. Ensure every major claim is backed by a real academic or scientific source.
4. Remove any redundant or unsubstantiated content to maintain clarity and conciseness.
5. Keep the revised content under 150 words.
6. Add a properly formatted “References” section at the end (not counted in the word limit), with full URLs for each source used.
7. Provide me link on every citation in format Link: String
8. Ensure the revised text is suitable for an academic audience, maintaining a formal tone and structure.

You must:
- Use Google Scholar, research repositories, or credible government/NGO sources for citations.
- Replace generic statements like “many studies show” with specific references.
- Suggest improved phrasing where appropriate to elevate academic tone and clarity.

Return only the revised text followed by a numbered “References” section.
"""


revisor_chain = actor_prompt_template.partial( first_instruction=revise_instructions) | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer")
