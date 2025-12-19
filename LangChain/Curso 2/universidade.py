import warnings

warnings.filterwarnings("ignore")

from langchain.tools import BaseTool
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.llms import Ollama
from pydantic import BaseModel, Field
from typing import ClassVar
import pandas as pd
import json


class ExtratorDeUniversidade(BaseModel):
    universidade: str = Field(description="O nome da universidade em minúsculo")


def busca_dados_da_universidade(universidade: str) -> dict:
    dados = pd.read_csv("documentos/universidades.csv")
    universidade = universidade.strip().lower()
    dados["NOME_FACULDADE"] = dados["NOME_FACULDADE"].str.strip().str.lower()
    dados_dessa_universidade = dados[dados["NOME_FACULDADE"] == universidade]
    if dados_dessa_universidade.empty:
        return {}
    return dados_dessa_universidade.iloc[0].to_dict()


def busca_dados_das_universidades() -> dict:
    dados = pd.read_csv("documentos/universidades.csv")
    return dados.to_dict()


class DadosDeUniversidade(BaseTool):
    name: ClassVar[str] = "DadosDeUniversidade"
    description: ClassVar[str] = (
        "Essa ferramenta extrai os dados de uma única universidade."
        "Passe para essa ferramenta como argumento o nome da universidade."
    )

    def _run(self, input: str) -> str:
        llm = Ollama(model="mistral")
        parser = JsonOutputParser(pydantic_object=ExtratorDeUniversidade)

        template = PromptTemplate(
            template="""
Você deve analisar a entrada a seguir e extrair **apenas a sigla ou o nome exato** da universidade que será usado para buscar dados em um banco. 
Sempre prefira a forma usada oficialmente no Brasil (ex: 'USP', 'UFRJ', 'UNICAMP') e escreva em letras maiusculas e sem acento.

Entrada:
-------------------
{input}
-------------------

Formato de saída:
{formato_saida}
""",
            input_variables=["input"],
            partial_variables={"formato_saida": parser.get_format_instructions()},
        )

        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input": input})
        universidade = resposta["universidade"]

        if isinstance(universidade, list):
            universidade = universidade[0]

        universidade = str(universidade).strip().lower()
        dados = busca_dados_da_universidade(universidade)
        return json.dumps(dados)

    def run(self, input: str) -> str:
        return self._run(input)


class TodasUniversidades(BaseTool):
    name: ClassVar[str] = "TodasUniversidades"
    description: ClassVar[str] = (
        "Carrega os dados de todas as universidades. "
        "Esta ferramenta não precisa de entrada, mas deve receber uma string vazia."
    )

    def _run(self, input: str) -> str:
        universidades = busca_dados_das_universidades()
        return json.dumps(universidades)

    def run(self, input: str) -> str:
        return self._run(input)
