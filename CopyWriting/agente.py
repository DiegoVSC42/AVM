from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_ollama import OllamaLLM
from langchain import hub


class AgenteOllama:
    def __init__(self, tools):
        self.tools = tools

        self.llm = OllamaLLM(model="mistral", temperature=0.5)
        prompt = hub.pull("hwchase17/react")

        agent = create_react_agent(llm=self.llm, tools=self.tools, prompt=prompt)

        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
        )

    def perguntar(self, pergunta: str) -> str:
        try:
            resposta = self.agent_executor.invoke({"input": pergunta})
            return resposta["output"]
        except Exception as e:
            return f"Ocorreu um erro ao processar a pergunta: {str(e)}"
