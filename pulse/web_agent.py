from agents import Agent, WebSearchTool
from pulse.summary_agent import summary_agent

web_agent = Agent(
    name = 'web_agent',
    instructions = """
    You are a web research agent for a clinical Q/A system. 
    Your job is to search the web for the answer to the question then handoff to the summary agent.
    You will be given a question and you will need to search the web for the answer. 
    You will need to use the web to find the answer to the question. 
    Return the answer in the natural language. 
    Provide as much detail and information as possible.

    ALWAYS handoff to the summary agent after you have searched the web.
    """,
    model = "gpt-4.1-mini", 
    tools = [WebSearchTool()],
    handoffs = [summary_agent],
)