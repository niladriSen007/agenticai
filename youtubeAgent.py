from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
from phi.model.groq import Groq

agent = Agent(
  name="YouTube Agent",
    role="YouTube Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YouTubeTools(get_video_captions=True)],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=2-JV8UxegWE", markdown=True,stream=True)
