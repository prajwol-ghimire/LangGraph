# LLM Agent Workflow using State Machine
```Langchain + LangGraph + LangSmith + Agents + Functions```

Built with LangGraph, LangChain, and LLM agents, this system demonstrates how structured autonomy can be achieved without relying entirely on human intervention.

---

## What This Project Is

Level 5 Autonomy where Decide output steps and which Steps to Take is decided by LLM itself for every Human Language NLP processing and LLMS Binds

```NLP +  LLM```

![Levels of autonomy in LLM applications](/Images/LevelsofAutonomy.png)


## Reflection vs Reflexion Agents

| Feature          | Reflection Agent                             | Reflexion Agent                              |
|------------------|----------------------------------------------|----------------------------------------------|
| How it learns    | Thinks about its own decisions               | Learns from past mistakes and tries again    |
| Feedback         | Uses self-review or prompts                  | Uses success/failure feedback                |
| Adaptability     | Somewhat flexible                            | Very flexible and improves over time         |
| Memory           | Optional or short-term                       | Keeps memory of what worked and what didn’t  |
| Goal             | Improve reasoning                            | Get better at solving tasks step by step     |
| Inspired by      | Human self-reflection                        | Trial-and-error learning like humans do      |
| Example          | [GraphVisulaization](GraphVisulaization) is a Reflection Agent. | [ReflexionAgent](ReflexionAgent) is a Reflexion Agent.|


![Reflexion Agent](/Images/Reflexion.png)



## State and Message in LangGraph

1. State in LangGraph

    A state is the shared memory or data context that is passed between nodes in a graph.
        
            state = {
                "user_input": "Where is the Eiffel Tower?",
                "tool_results": {},
                "final_answer": None
            }

2. Message in LangGraph

    A message is a unit of information that is passed between nodes—often the data that triggers the next step in the graph.

        message = {
            "role": "user",
            "content": "Show me restaurants in Paris."
        }

## ReAct agents

`initialize_agent()` class contains two method that are described as:

- `create_react_agent`: A Langchain helper that creates a ReAct-style agent (Reasoning + Acting) using a language model and a set of tools. It lets the agent reason step-by-step and call tools as needed.

- `AgentExecutor`: A class in Langchain that executes agents—it manages the loop of reasoning, tool usage, and final answer generation based on the agent’s logic.

## Memory Chat Bot

### CheckPointers:

- Way to save State or workflow at specifc point during execution
- Used For Memory in chatbot 

### Thread ID:

- Simply a unique identider for specifc conversation or workflow execution
- Thing like sessionID for every own chat.

### Human In Loop:

In [ChatBotwithToolOutput](ChatBotwithToolOutput) we got error when asking for Favorite Flavour of Icecream since tool used same function for Ram and hari when asking for Favorite Flavour. Human in Loop remove the ambigutiy to LLM and Ask the validation of response to the user and save into memory.

- Reviewing tool calls
- Validating LLMS Ouputs

#### Design Patterns in Human In Loop

1. Approve and reject:

    Depending on Human approval or rejection with the action or take alternative path.

    ![Approveorreject](/Images/Approveorreject.png)

2. Review and Edit State

    A human can review and edit the mistake and correct the mistake or update the state information. We are updating the state here not tool itself.

    ![ReviewAndEditState](/Images/ReviewAndEditState.png)

3. Review Tool calls

    A human can review and eddit LLM output befor processing. It is needed for Tools calls by the LLMs are sensative and need approval such as To change username of user asking the secert code of something that only authorized user and LLM thread knows

    ![ReviewToolCalls](/Images/ReviewToolCalls.png)

#### Example
For a Content creating AI for social Media and Post Automatiaclly with API method Call 
    ![ReviewByHuman](/Images/ReviewByHuman.png)