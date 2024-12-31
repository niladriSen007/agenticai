import phi.api
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi
import os
from phi.playground import Playground, serve_playground_app

web_search_agent = Agent(
    name="Web Search Analyst",
    role="Web Search Analyst",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    markdown=True,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),DuckDuckGo()],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible as a Web search agent."],
)


financial_agent = Agent(
    name="Financial Analyst",
    role="Financial Analyst",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    markdown=True,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,technical_indicators=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
)

app = Playground(agents=[web_search_agent, financial_agent]).get_app()
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)