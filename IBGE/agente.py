import warnings

warnings.filterwarnings("ignore")

from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.llms import Ollama
from langchain import hub

import warnings

warnings.filterwarnings("ignore")

from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.llms import Ollama
from langchain import hub
from langchain.prompts import PromptTemplate

import municipio
from langchain.tools import BaseTool
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate


class AgenteOllama:
    def __init__(self):
        self.dados_de_municipio = municipio.DadosDeMunicipio()

        self.tools = [
            Tool(
                name=self.dados_de_municipio.name,
                func=self.dados_de_municipio.run,
                description=self.dados_de_municipio.description,
            ),
        ]

        self.llm = OllamaLLM(model="mistral", temperature=0.5)

        # Aqui você obtém o prompt padrão do LangChain Hub para agentes React
        prompt = hub.pull("hwchase17/react")

        agent = create_react_agent(
            llm=self.llm, tools=self.tools, prompt=prompt  # <- adiciona este argumento
        )

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
