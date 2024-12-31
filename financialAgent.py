from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

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

multi_ai_agent = Agent(
  team=[web_search_agent, financial_agent],
   model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
  name="Multi AI Agent",
  role="Multi AI Agent",
  instructions=["Format your response using markdown and use tables to display data where possible."],
  description="You are an investment analyst that researches stock prices, analyst recommendations, stock fundamentals, and technical indicators.",
  markdown=True,
  show_tool_calls=True,
)

web_search_agent.print_response("Summary of stock prices, analyst recommendations, stock fundamentals, and technical indicators for Infosys.",stream=True)
financial_agent.print_response("Summary of stock prices, analyst recommendations, stock fundamentals, and technical indicators for Infosys.",stream=True)

