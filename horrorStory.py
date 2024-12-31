from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.website import WebsiteTools

agent = Agent(
  name="Horror Story Agent",
  role="Horror Story Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    markdown=True,
    description="You are a horror story agent that shares 2 sentence horror stories",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    tools=[WebsiteTools(knowledge_base="https://dyatmika.org/students/my-favourite-short-scary-stories/")]
)

agent.print_response("Share a 2 sentence horror story.",stream=True)

