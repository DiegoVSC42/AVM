import warnings

warnings.filterwarnings("ignore")

from langchain_core.runnables import Runnable
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.llms import Ollama
from langchain import hub
from langchain.prompts import PromptTemplate

from estudante import DadosDeEstudante, PerfilAcademico
from universidade import DadosDeUniversidade, TodasUniversidades

import warnings

warnings.filterwarnings("ignore")

from langchain_core.runnables import Runnable
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.llms import Ollama
from langchain import hub
from langchain.prompts import PromptTemplate

from estudante import DadosDeEstudante, PerfilAcademico
from universidade import DadosDeUniversidade, TodasUniversidades


class AgenteOllama:
    def __init__(self):
        # Instancia as ferramentas
        self.dados_de_estudante = DadosDeEstudante()
        self.perfil_academico = PerfilAcademico()
        self.dados_de_universidade = DadosDeUniversidade()
        self.todas_universidades = TodasUniversidades()

        self.tools = [
            Tool(
                name=self.dados_de_estudante.name,
                func=self.dados_de_estudante.run,
                description=self.dados_de_estudante.description,
            ),
            Tool(
                name=self.perfil_academico.name,
                func=self.perfil_academico.run,
                description=self.perfil_academico.description,
            ),
            Tool(
                name=self.dados_de_universidade.name,
                func=self.dados_de_universidade.run,
                description=self.dados_de_universidade.description,
            ),
            Tool(
                name=self.todas_universidades.name,
                func=self.todas_universidades.run,
                description=self.todas_universidades.description,
            ),
        ]

        self.llm = Ollama(model="mistral")

        base_prompt = hub.pull("hwchase17/react")

        # custom_prefix = (
        #     "Sempre responda no mesmo idioma da pergunta original. "
        #     "Se a pergunta estiver em português, responda em português.\n\n"
        # )

        # custom_prompt = PromptTemplate(
        #     input_variables=base_prompt.input_variables,
        #     template=custom_prefix + base_prompt.template,
        # )

        agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=base_prompt,
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
