import warnings

warnings.filterwarnings("ignore")
from langchain.tools import BaseTool
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import OllamaLLM
import pandas as pd
import json

from langchain.tools import BaseTool
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

from typing import ClassVar


def busca_dados_de_municipio(municipio: str) -> dict:
    dados = pd.read_csv(
        "documentos/MUNICÍPIOS.csv",
        skiprows=1,
        sep=",",
        thousands=".",
        encoding="utf-8",
    )
    dados["NOME DO MUNICÍPIO"] = dados["NOME DO MUNICÍPIO"].str.lower().str.strip()
    municipio = municipio.lower().strip()
    dados_com_esse_municipio = dados[dados["NOME DO MUNICÍPIO"] == municipio]
    if dados_com_esse_municipio.empty:
        return {}
    return dados_com_esse_municipio.iloc[0].to_dict()


class DadosDeMunicipio(BaseTool):
    name: ClassVar[str] = "DadosDeMunicipio"
    description: ClassVar[
        str
    ] = """
    Essa ferramenta extrai os dados de um municipio do IBGE sobre ESTIMATIVAS DA POPULAÇÃO RESIDENTE NOS MUNICÍPIOS BRASILEIROS COM DATA DE REFERÊNCIA EM 1º DE JULHO DE 2024
        Essa tabela contem algumas colunas sendo elas:
            UF : Sigla do estado
            COD. UF : Código do estado
            COD. MUNIC : Código do múnicipio
            NOME DO MUNICÍPIO : Nome do múnicipio inteiro com acentos e espaçamentos(quando passível)
            POPULAÇÃO ESTIMADA : População estimada neste período
    """

    class ExtratorDeMunicipio(BaseModel):
        municipio: str = Field(description="Nome do município informado")

    def _run(self, input: str) -> str:
        llm = OllamaLLM(model="mistral")
        parser = JsonOutputParser(pydantic_object=self.ExtratorDeMunicipio)
        template = PromptTemplate(
            template="""
Extraia apenas o nome do município presente na entrada abaixo.
Retorne SOMENTE um JSON **válido** conforme o formato indicado, com aspas duplas (").
Sem explicações, sem texto extra, sem comentários. Apenas o JSON puro.

Entrada:
{input}

Formato de saída:
{formato_saida}
""",
            input_variables=["input"],
            partial_variables={"formato_saida": parser.get_format_instructions()},
        )

        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input": input})
        municipio = resposta.get("municipio")

        if isinstance(municipio, list):
            municipio = municipio[0]

        municipio = str(municipio).strip().lower()
        dados = busca_dados_de_municipio(municipio)
        return json.dumps(dados)
