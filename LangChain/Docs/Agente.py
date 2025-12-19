from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

model = ChatOllama(model="mistral")
memory = MemorySaver()
search = TavilySearch(tavily_api_key="SUA_CHAVE_AQUI", max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}
input_message = {
    "role": "user",
    "content": "Hello i am bob and live in SF. What's the weather where I live in celsius?",
}

for step in agent_executor.stream(
    {"messages": [input_message]}, config, stream_mode="values"
):
    step["messages"][-1].pretty_print()
