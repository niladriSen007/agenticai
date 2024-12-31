from phi.agent import Agent
from phi.tools.googlesearch import GoogleSearch
from phi.model.groq import Groq

agent = Agent(
    tools=[GoogleSearch()],
     model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    description="You are a news agent that helps users find the latest news.",
    instructions=[
        "Given a topic by the user, respond with 4 latest news items about that topic.",
        "Search for 10 news items and select the top 4 unique items.",
        "Search in English and in Bengali.",
    ],
    show_tool_calls=True,
    debug_mode=True,
)
agent.print_response("Indian Cricket", markdown=True)
